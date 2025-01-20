from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory

def generate_launch_description():

    amcl_dir = os.path.join(get_package_share_directory('localization_server'),'config', 'amcl_config.yaml')
    map_dir = os.path.join(get_package_share_directory('map_server'), 'config', 'neobotix_area.yaml')
    my_world_dir = get_package_share_directory('my_gazebo_world')


    start_gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        os.path.join(my_world_dir, 'launch', 'my_world1.launch.py')
    ))

    start_map = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{'use_sim_time': True}, 
                    {'yaml_filename':map_dir}]
    ) 

    start_nav2 = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_localization',
        output='screen',
        parameters=[{'use_sim_time': True},
                    {'autostart': True},
                    {'node_names': ['map_server','amcl']}]
    )

    start_amcl = Node(
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        output='screen',
        parameters=[amcl_dir]
    )

   

    ld = LaunchDescription()
    ld.add_action(start_gazebo)
    ld.add_action(start_map)
    ld.add_action(start_amcl)
    ld.add_action(start_nav2)

    return ld