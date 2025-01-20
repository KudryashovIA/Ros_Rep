import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Moving_robot(Node):

    def __init__(self):
        super().__init__('moving_robot')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)

    def moving_callback(self):
        msg = Twist()
        msg.linear.x = 0.2
        msg.angular.z = 0.3
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)
            
def main(args=None):
    rclpy.init(args=args)
    simple_publisher = Moving_robot()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()