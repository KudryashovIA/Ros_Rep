from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='multithreading_ros2_examples',
            executable='multithreading_movement_server_and_calculation_server',
            output='screen',
            emulate_tty=True),
    ])