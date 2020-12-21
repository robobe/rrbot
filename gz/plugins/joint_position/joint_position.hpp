#ifndef GAZEBO_PLUGINS_JOINT_VELOCTY_HH
#define GAZEBO_PLUGINS_JOINT_VELOCTY_HH

#include <gazebo/gazebo.hh>
#include <gazebo/physics/Joint.hh>
#include <gazebo/physics/JointController.hh>
#include <gazebo/physics/Model.hh>
#include <gazebo/physics/PhysicsTypes.hh>

namespace gazebo
{
    class JointPositionPluginPrivate;

    class JointPositionPlugin : public ModelPlugin
    {
    public:
        JointPositionPlugin();

    public:
        virtual void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf);

    public:
        virtual void Init();

    private:
        void OnUpdate();

    private:
        void OnStringMsg(ConstGzStringPtr &_msg);

    private:
        std::unique_ptr<JointPositionPluginPrivate> dataPtr;
    };
} // namespace gazebo
#endif