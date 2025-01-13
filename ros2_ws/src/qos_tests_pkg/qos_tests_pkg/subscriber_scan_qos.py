import rclpy
from rclpy.node import Node
import rclpy.qos
from std_msgs.msg import String
from rclpy.qos import ReliabilityPolicy, QoSProfile
from sensor_msgs.msg import LaserScan
from rclpy.duration import Duration

class SubscriberScan(Node):

    def __init__(self):

        super().__init__('subscriber_scan')

      
        self.subscriber = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            depth=10,
            liveliness = rclpy.qos.LivelinessPolicy.AUTOMATIC)
        )
        self.subscriber
        
        self.laser_forward = 0

    def listener_callback(self, msg: LaserScan):
        self.get_logger().info("I heard: '%s'" % msg.ranges)


def main(args=None):
    rclpy.init(args=args)
    subscriber_scan = SubscriberScan()
    rclpy.spin(subscriber_scan)
    subscriber_scan.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()