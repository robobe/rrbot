// http://gazebosim.org/tutorials?tut=guided_i5


#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <gazebo/msgs/msgs.hh>
#include <gazebo/transport/transport.hh>
#include "joint_velocity.hpp"
namespace gazebo
{
    class JointVelocityPluginPrivate
    {
    public:
        std::vector<event::ConnectionPtr> connections;
        physics::ModelPtr model;
        common::PID pid;
        physics::JointPtr joint1;
        transport::NodePtr node;
        transport::SubscriberPtr sub;
        
        double command = IGN_PI_2;
        common::Time lastUpdateTime;
    };

    JointVelocityPlugin::JointVelocityPlugin()
        : dataPtr(new JointVelocityPluginPrivate)
    {
        this->dataPtr->pid.Init(10, 0, 0, 0, 0, 100.0, -100.0);
        gzmsg << "constructor\n";
    }

    void JointVelocityPlugin::Init()
    {
        this->dataPtr->node = transport::NodePtr(new transport::Node());
        this->dataPtr->node->Init(this->dataPtr->model->GetWorld()->Name());
        this->dataPtr->lastUpdateTime =
            this->dataPtr->model->GetWorld()->SimTime();
        std::string topic = "/joint/cmd";
        this->dataPtr->sub = this->dataPtr->node->Subscribe(topic,
                                                            &JointVelocityPlugin::OnStringMsg, this);
        this->dataPtr->connections.push_back(event::Events::ConnectWorldUpdateBegin(
          std::bind(&JointVelocityPlugin::OnUpdate, this)));
        gzmsg << "init\n";
    }

    void JointVelocityPlugin::Load(physics::ModelPtr _model,
                                sdf::ElementPtr _sdf)
    {
        this->dataPtr->model = _model;
        std::string jointName = "joint2";
        if (_sdf->HasElement("joint2"))
        {
            jointName = _sdf->Get<std::string>("joint2");
        }
        this->dataPtr->joint1 = this->dataPtr->model->GetJoint(jointName);
        this->dataPtr->model->GetJointController()->SetVelocityPID(
            this->dataPtr->joint1->GetScopedName(), this->dataPtr->pid);
            this->dataPtr->model->GetJointController()->SetVelocityTarget(
      this->dataPtr->joint1->GetScopedName(), 1.0);
        gzmsg<<"load\n";
    }

    void JointVelocityPlugin::OnUpdate()
    {
        // gzmsg << "update\n";
       
    }

    void JointVelocityPlugin::OnStringMsg(ConstGzStringPtr &_msg)
    {
        auto vel = atof(_msg->data().c_str());
        this->dataPtr->model->GetJointController()->SetVelocityTarget(
          this->dataPtr->joint1->GetScopedName(), vel);
        
        gzmsg << _msg->data().c_str() << std::endl;
    }
    GZ_REGISTER_MODEL_PLUGIN(JointVelocityPlugin)
} // namespace gazebo