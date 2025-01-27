from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='parameter_tests',
            executable='param_odom_and_scan',
            name='param_odom_and_scan',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'get_odom_data': True},
                {'get_laser_data': True}
            ]
        )
    ])