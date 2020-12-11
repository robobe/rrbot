#ifndef GAZEBO_PLUGINS_JOINT_FORCE_HH
#define GAZEBO_PLUGINS_JOINT_FORCE_HH

#include <gazebo/gazebo.hh>
#include <gazebo/physics/Joint.hh>
#include <gazebo/physics/JointController.hh>
#include <gazebo/physics/Model.hh>
#include <gazebo/physics/PhysicsTypes.hh>

namespace gazebo
{
  class JointForcePluginPrivate;

  class JointForcePlugin : public ModelPlugin
  {
  public:
    JointForcePlugin();

  public:
    virtual void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf);

  public:
    virtual void Init();

  private:
    void OnUpdate();

  private:
    std::unique_ptr<JointForcePluginPrivate> dataPtr;
  };
} // namespace gazebo
#endif