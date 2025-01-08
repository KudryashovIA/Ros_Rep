from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='remapping_pkg',
            executable='simple_remapper_exe',
            output='screen',
            emulate_tty=True, 
            remappings=[("/in_my_scan", "/scan"),("/out_cmd_vel","/cmd_vel")]),
    ])