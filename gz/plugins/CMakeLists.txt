
add_library(JointForcePlugin SHARED joint_force/joint_force.cpp)
target_link_libraries(JointForcePlugin ${GAZEBO_LIBRARIES})
install(TARGETS JointForcePlugin DESTINATION ${PROJECT_SOURCE_DIR}/bin)

add_library(JointVelocityPlugin SHARED joint_velocity/joint_velocity.cpp)
target_link_libraries(JointVelocityPlugin ${GAZEBO_LIBRARIES})
install(TARGETS JointVelocityPlugin DESTINATION ${PROJECT_SOURCE_DIR}/bin)