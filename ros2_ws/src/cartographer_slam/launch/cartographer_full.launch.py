from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory


def generate_launch_description():

   
    cartographer_dir =get_package_share_directory('cartographer_slam')
    my_world_dir = get_package_share_directory('my_gazebo_world')

    cartographer_start = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        os.path.join(cartographer_dir,'launch', 'cartographer.launch.py' )    
    ))
    # moving_start = IncludeLaunchDescription(PythonLaunchDescriptionSource(
    #     os.path.join(cartographer_dir, 'launch', 'moving_robot.launch.py')
    # ))
    start_gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        os.path.join(my_world_dir, 'launch', 'my_world1.launch.py')
    ))
   
    
    return LaunchDescription([
        cartographer_start,
        #moving_start,
        start_gazebo
    ])
    

