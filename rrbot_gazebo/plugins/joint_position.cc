#include <functional>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <ignition/math/Vector3.hh>

namespace gazebo
{
    class JointPositionPlugin : public ModelPlugin
    {
    public:
        void Load(physics::ModelPtr _parent, sdf::ElementPtr /*_sdf*/)
        {
            // Store the pointer to the model
            this->model = _parent;
            this->lastControllerUpdateTime = this->model->GetWorld()->SimTime();
            this->pid.Init(200, 20, 2, 1000, -1000, 1000, -1000);
            this->updateConnection = event::Events::ConnectWorldUpdateBegin(
                std::bind(&JointPositionPlugin::OnUpdate, this));
        }

        // Called by the world update start event
    public:
        void OnUpdate()
        {
            const gazebo::common::Time curTime = this->model->GetWorld()->SimTime();
            const double _dt = (curTime - this->lastControllerUpdateTime).Double();
            this->lastControllerUpdateTime = this->model->GetWorld()->SimTime();
            const double pos = this->model->GetJoint("joint1")->Position(0);
            const double error = pos - 1.575;
            const double force = this->pid.Update(error, _dt);

            this->model->GetJoint("joint1")->SetForce(0, force);
        }

        // Pointer to the model
    private:
        physics::ModelPtr model;
        gazebo::common::Time lastControllerUpdateTime;
        common::PID pid;

        // Pointer to the update event connection
    private:
        event::ConnectionPtr updateConnection;
    };

    // Register this plugin with the simulator
    GZ_REGISTER_MODEL_PLUGIN(JointPositionPlugin)
}