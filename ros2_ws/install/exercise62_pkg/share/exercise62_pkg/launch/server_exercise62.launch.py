from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='exercise62_pkg',
            executable='server_exercise62',
            output='screen'),
    ])