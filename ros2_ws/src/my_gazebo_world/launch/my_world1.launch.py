# Моя карта

# import os
# from ament_index_python.packages import get_package_share_directory
# from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.substitutions import LaunchConfiguration


# def generate_launch_description():
#     # Путь к директориям пакетов
#     pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

#     # Путь к вашему миру
#     world = os.path.join(
#         get_package_share_directory('my_gazebo_world'),  # Замените на ваш пакет с миром
#         'worlds',
#         'test.sdf'  # Замените на ваш файл мира .sdf или .world
#     )

#     # Запуск сервера Gazebo с вашим миром
#     gzserver_cmd = ExecuteProcess(
#         cmd=['gazebo', '--verbose', world],
#         name='gzserver',
#         output='screen'
#     )

#     # Запуск клиента Gazebo
#     gzclient_cmd = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(
#             os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
#         )
#     )

#     # Создание LaunchDescription и добавление команд
#     ld = LaunchDescription()

#     # Добавляем команду для запуска сервера Gazebo
#     ld.add_action(gzserver_cmd)

#     # Добавляем команду для запуска клиента Gazebo
#     ld.add_action(gzclient_cmd)

#     return ld
#------------------------------------------------------------------------


import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    launch_file_dir = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    x_pose = LaunchConfiguration('x_pose', default='0.0')
    y_pose = LaunchConfiguration('y_pose', default='0.0')

    world = os.path.join(
        get_package_share_directory('my_gazebo_world'),
        'worlds',
        'test.sdf'
    )

    # rviz = os.path.join(
    #     get_package_share_directory('my_gazebo_world'),
    #     'rviz',
    #     'my_rviz.rviz'
    # )

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )

    robot_state_publisher_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'robot_state_publisher.launch.py')
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    spawn_turtlebot_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'spawn_turtlebot3.launch.py')
        ),
        launch_arguments={
            'x_pose': x_pose,
            'y_pose': y_pose
        }.items()
    )

    rviz_cmd = ExecuteProcess(
        cmd=['ros2', 'run', 'rviz2', 'rviz2', '-d', '/home/ivan/work/Ros_Rep/ros2_ws/src/my_gazebo_world/rviz/my_rviz.rviz'],
        name='rviz',
        output='screen'
    )

    ld = LaunchDescription()

    # Add the commands to the launch description
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)
    ld.add_action(robot_state_publisher_cmd)
    ld.add_action(spawn_turtlebot_cmd)
    ld.add_action(rviz_cmd)

    return ld