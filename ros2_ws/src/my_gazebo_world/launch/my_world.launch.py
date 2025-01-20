# import os
# from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument, ExecuteProcess
# from launch.substitutions import LaunchConfiguration

# def generate_launch_description():
#     return LaunchDescription([
#         # Объявление аргумента для пути к SDF файлу
#         DeclareLaunchArgument(
#             'world',
#             default_value='/home/ivan/work/Ros_Rep/ros2_ws/src/my_gazebo_world/worlds/test.sdf',
#             description='Path to the Gazebo world file'
#         ),
        
#         # Запуск gzserver с указанием пути к миру
#         ExecuteProcess(
#             cmd=['gazebo', '--verbose', LaunchConfiguration('world')],
#             output='screen'
#         ),
#     ])

import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
import launch

def generate_launch_description():
    # Указываем путь к вашему миру в Gazebo
    sdf_world_path = os.path.join(
        get_package_share_directory('my_gazebo_world'),
        'worlds',
        'test.sdf'
    )

    return LaunchDescription([
        # Запуск Gazebo с вашим миром
        Node(
            package='gazebo_ros',
            executable='/usr/bin/gzserver',
            output='screen',
            arguments=['--verbose', sdf_world_path]
        ),
        
        # Запуск клиента Gazebo для отображения
        Node(
            package='gazebo_ros',
            executable='/usr/bin/gzclient',
            output='screen'
        ),

        # Запуск модели TurtleBot3 в Gazebo
        Node(
            package='turtlebot3_gazebo',
            executable='turtlebot3_world',
            name='turtlebot3_in_gazebo',
            output='screen',
            parameters=[{
                'use_sim_time': True
            }],
        ),
    ])
