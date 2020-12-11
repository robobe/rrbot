#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <gazebo/msgs/msgs.hh>
#include <gazebo/transport/transport.hh>
#include "joint_force.hpp"
namespace gazebo
{
    class JointForcePluginPrivate
    {
    public:
        std::vector<event::ConnectionPtr> connections;
        physics::ModelPtr model;
        common::PID pid;
        physics::JointPtr joint1;
        transport::NodePtr node;
        transport::SubscriberPtr sub;
        void OnStringMsg(ConstGzStringPtr &_msg);
        double command = IGN_PI_2;
        common::Time lastUpdateTime;
    };

    JointForcePlugin::JointForcePlugin()
        : dataPtr(new JointForcePluginPrivate)
    {
        this->dataPtr->pid.Init(10, 0, 0, 0, 0, 100.0, -100.0);
        gzmsg << "constructor\n";
    }

    void JointForcePlugin::Init()
    {
        this->dataPtr->node = transport::NodePtr(new transport::Node());
        this->dataPtr->node->Init(this->dataPtr->model->GetWorld()->Name());
        this->dataPtr->lastUpdateTime =
            this->dataPtr->model->GetWorld()->SimTime();
        std::string topic = "/joint/cmd";
        this->dataPtr->sub = this->dataPtr->node->Subscribe(topic,
                                                            &JointForcePluginPrivate::OnStringMsg, this->dataPtr.get());
        this->dataPtr->connections.push_back(event::Events::ConnectWorldUpdateBegin(
          std::bind(&JointForcePlugin::OnUpdate, this)));
        gzmsg << "init\n";
    }
    void JointForcePlugin::Load(physics::ModelPtr _model,
                                sdf::ElementPtr _sdf)
    {
        this->dataPtr->model = _model;
        std::string jointName = "joint2";
        if (_sdf->HasElement("joint2"))
        {
            jointName = _sdf->Get<std::string>("joint2");
        }
        this->dataPtr->joint1 = this->dataPtr->model->GetJoint(jointName);
        gzmsg<<"load\n";
    }

    void JointForcePlugin::OnUpdate()
    {
        // gzmsg << "update\n";
        if (!this->dataPtr->joint1)
            return;

        double angle = this->dataPtr->joint1->Position(0);
        // gzmsg << "angel:" << angle << "\n";
        common::Time time = this->dataPtr->model->GetWorld()->SimTime();
        // gzmsg << "time:" << time.FormattedString() << "\n"; 
        if (time < this->dataPtr->lastUpdateTime)
        {
            this->dataPtr->lastUpdateTime = time;
            return;
        }
        else if (time > this->dataPtr->lastUpdateTime)
        {
            double dt = (this->dataPtr->lastUpdateTime - time).Double();
            double error = angle - this->dataPtr->command;
            double force = this->dataPtr->pid.Update(error, dt);
            gzmsg << "error: " << error << "force: " << force << "\n";
            this->dataPtr->joint1->SetForce(0, force);
            this->dataPtr->lastUpdateTime = time;
        }
    }

    void JointForcePluginPrivate::OnStringMsg(ConstGzStringPtr &_msg)
    {
        this->command = atof(_msg->data().c_str());
        gzmsg << _msg->data().c_str() << std::endl;
    }
    GZ_REGISTER_MODEL_PLUGIN(JointForcePlugin)
} // namespace gazebo