import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ivan/work/Ros_Rep/ros2_ws/install/multithreading_ros2_examples'