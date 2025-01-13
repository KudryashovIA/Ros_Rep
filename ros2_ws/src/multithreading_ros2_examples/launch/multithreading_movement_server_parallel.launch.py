from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='multithreading_ros2_examples',
            executable='multithreading_movement_server_parallel',
            output='screen',
            emulate_tty=True),
    ])