import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess


def generate_launch_description():
    # Получаем путь к файлу карты
    map_dir = os.path.join(
        get_package_share_directory('map_server'),
        'config',
        'neobotix_area.yaml'
    )

    map_server = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'yaml_filename': map_dir
        }]
    )

    rviz_cmd = ExecuteProcess(
        cmd=['ros2', 'run', 'rviz2', 'rviz2'],
        name='rviz',
        output='screen'
    )
   
    lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_mapper',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'autostart': True,
            'node_names': ['map_server']
        }]
    )
    ld = LaunchDescription()

    ld.add_action(map_server)
    ld.add_action(lifecycle_manager)
    ld.add_action(rviz_cmd)

    return ld