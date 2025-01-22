import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PointStamped

class Pub_Goal_pose(Node):
    def __init__(self):
        super().__init__('publish_pose')

        self.publisher = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 10)

    def pub_pose(self):
        msg = PoseWithCovarianceStamped()
        msg.header.frame_id = '/map'
        msg.pose.pose.position.x = -5.0
        msg.pose.pose.position.x = -5.0
        msg.pose.pose.orientation.w = 1.0
        self.publisher.publish(msg)

        self.get_logger().info('Publishing:\n X = -5.0, Y = -5.0, W = 1.0')

def main(args=None):
    rclpy.init(args=args)
    publisher_pose = Pub_Goal_pose()
    publisher_pose.pub_pose()  
    rclpy.spin_once(publisher_pose)  
    publisher_pose.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
