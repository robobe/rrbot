
. /usr/share/gazebo/setup.sh
name=$(basename `pwd`)
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:`pwd`/${name}_description/models
export GAZEBO_RESOURCE_PATH=$GAZEBO_RESOURCE_PATH:`pwd`/${name}_gazebo/worlds
export GAZEBO_PLUGIN_PATH=$GAZEBO_PLUGIN_PATH:`pwd`/${name}_gazebo/bin