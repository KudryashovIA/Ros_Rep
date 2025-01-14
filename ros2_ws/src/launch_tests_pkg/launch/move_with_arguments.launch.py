import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():

    turning_speed_arg = DeclareLaunchArgument(
        "turning_speed", default_value="1.0"
    )
    forwards_speed_arg = DeclareLaunchArgument(
        "forwards_speed", default_value="1.0"
    )

    turning_speed_f = LaunchConfiguration('turning_speed')
    forwards_speed_f = LaunchConfiguration('forwards_speed')

    move_robot_node = Node(
        package='launch_tests_pkg',
        executable='move_robot_with_arguments_exe',
        output='screen',
        name='move_robot_node',
        emulate_tty=True,
        arguments=["-turning_speed", turning_speed_f,
                   "-forwards_speed", forwards_speed_f,
                   ]

    )

    # create and return launch description object
    return LaunchDescription(
        [
            turning_speed_arg,
            forwards_speed_arg,
            move_robot_node
        ]
    )