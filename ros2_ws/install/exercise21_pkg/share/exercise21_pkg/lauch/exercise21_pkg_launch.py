from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='exercise21_pkg',
            executable='exercise21',
            output='screen'),
    ])