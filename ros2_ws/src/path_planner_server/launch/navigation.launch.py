from launch import LaunchDescription
import os
from ament_index_python import get_package_share_directory
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    amcl_dir = os.path.join(get_package_share_directory('localization_server'),'config', 'amcl_config.yaml')
    map_dir = os.path.join(get_package_share_directory('map_server'), 'config', 'neobotix_area.yaml')
    bt_navigator_dir = os.path.join(get_package_share_directory('path_planner_server'), 'config', 'bt_navigator.yaml')
    controller_dir = os.path.join(get_package_share_directory('path_planner_server'), 'config', 'controller.yaml')
    planner_dir = os.path.join(get_package_share_directory('path_planner_server'), 'config', 'planner_server.yaml')
    recovery_dir = os.path.join(get_package_share_directory('path_planner_server'), 'config', 'recovery.yaml')
    
    my_world_dir = get_package_share_directory('my_gazebo_world')

    initial_dir = get_package_share_directory('path_planner_server')
    action_client_dir = get_package_share_directory('path_planner_server')

    common_parameters = [{'use_sim_time': True}]

    start_gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        os.path.join(my_world_dir, 'launch', 'my_world1.launch.py')
    ))

    start_map = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{'yaml_filename': map_dir}] + common_parameters
    )

    start_amcl = Node(
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        output='screen',
        parameters=[amcl_dir] + common_parameters
    )

    start_pose = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        os.path.join(initial_dir, 'launch', 'pathplanner_full_init.launch.py')
    ))

    start_action_client = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        os.path.join(action_client_dir, 'launch', 'action_client.launch.py')
    ))

    start_navigator = Node(
        package='nav2_bt_navigator',
        executable='bt_navigator',
        name='bt_navigator',
        output='screen',
        parameters=[bt_navigator_dir] + common_parameters
    )

    start_controller = Node(
        package='nav2_controller',
        executable='controller_server',
        name='controller_server',
        output='screen',
        parameters=[controller_dir] + common_parameters
    )

    start_planner = Node(
        package='nav2_planner',
        executable='planner_server',
        name='planner_server',
        output='screen',
        parameters=[planner_dir] + common_parameters
    )

    start_recovery = Node(
        package='nav2_behaviors',
        executable='behavior_server',
        name='recoveries_server',
        output='screen',
        parameters=[recovery_dir] + common_parameters
    )

    start_nav2_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager',
        output='screen',
        parameters=[
            {'use_sim_time': True},
            {'autostart': True},
            {'node_names': ['map_server', 'amcl', 'bt_navigator', 
                            'controller_server', 'planner_server', 'recoveries_server']}
        ]
    )

    ld = LaunchDescription()
    ld.add_action(start_gazebo)
    ld.add_action(start_map)
    ld.add_action(start_amcl)
    ld.add_action(start_pose)
    ld.add_action(start_action_client)
    ld.add_action(start_navigator)
    ld.add_action(start_controller)
    ld.add_action(start_planner)
    ld.add_action(start_recovery)
    ld.add_action(start_nav2_manager)

    return ld