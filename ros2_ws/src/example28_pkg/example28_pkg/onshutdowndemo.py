import rclpy
from rclpy.node import Node
import time

from std_msgs.msg import String
from geometry_msgs.msg import Twist


class Test(Node):

    def __init__(self):
        super().__init__('test')

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.cmd = Twist()
        self.turn()

    def turn(self):
        self.get_logger().info("TURNING....")
        self.cmd.linear.x = 0.5
        self.cmd.angular.z = 0.5
        self.publisher_.publish(self.cmd)  
    
    def stop(self):
        self.get_logger().info("STOPPING....")
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publisher_.publish(self.cmd)
        self.get_logger().info("STOPPED")

    def __del__(self):
        self.stop()

def main(args=None):
    rclpy.init(args=args)

    node_test = Test()
    rclpy.spin(node_test)

    node_test.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()