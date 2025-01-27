import rclpy
import rclpy.node
from rcl_interfaces.msg import ParameterDescriptor
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry


class Parameters(rclpy.node.Node):
    def __init__(self):
        super().__init__('param_odom_and_scan')
  
        odom_descriptor = ParameterDescriptor(description='OFF/ON display of laser data.')
        self.declare_parameter('get_odom_data', True, odom_descriptor)

        scan_descriptor = ParameterDescriptor(description='OFF/ON display of odom data.')
        self.declare_parameter('get_laser_data', True, scan_descriptor)

        self.laser_sub = self.create_subscription(LaserScan, '/scan', self.laser_callback, 10)
        self.omod_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

    def laser_callback(self, msg):

        if self.get_parameter('get_laser_data').value:
            laser_val = msg.ranges[len(msg.ranges) // 2]
            self.get_logger().info(f'Laser value: {laser_val}')

    def odom_callback(self, msg):
        if self.get_parameter('get_odom_data').value:
            x = msg.pose.pose.position.x
            y = msg.pose.pose.position.y
            self.get_logger().info(f'Position: X = {x}, Y = {y}')



def main():
    rclpy.init()
    node = Parameters()
    rclpy.spin(node)


if __name__ == '__main__':
    main()