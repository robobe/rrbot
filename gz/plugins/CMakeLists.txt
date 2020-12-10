# Find Gazebo
find_package(gazebo REQUIRED)
include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")

# Build our plugin
add_library(simple_sub SHARED simple/simple_sub.cpp)
target_link_libraries(simple_sub ${GAZEBO_libraries})
target_compile_features(simple_sub PRIVATE cxx_std_17)
install(TARGETS simple_sub DESTINATION ${PROJECT_SOURCE_DIR}/bin)


add_library(SetJointVelocityPlugin SHARED joint_plugin/JointPlugin.cpp)
target_link_libraries(SetJointVelocityPlugin ${GAZEBO_LIBRARIES})
install(TARGETS SetJointVelocityPlugin DESTINATION ${PROJECT_SOURCE_DIR}/bin)