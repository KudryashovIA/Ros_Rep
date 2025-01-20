from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cartographer_slam',
            executable='moving_robot_node',  # Зарегистрированная команда
            name='moving_robot_node',
            output='screen',
            parameters=[
                {'use_sim_time': True}
            ],
        )
    ])
