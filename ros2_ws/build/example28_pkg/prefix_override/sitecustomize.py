import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ivan/work/Ros_Rep/ros2_ws/install/example28_pkg'
