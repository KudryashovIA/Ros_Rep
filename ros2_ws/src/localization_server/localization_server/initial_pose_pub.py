import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PointStamped


class Publisher(Node):

    def __init__(self):
        super().__init__('initial_pose_pub_node')

        self.subscriber_ = self.create_subscription(PointStamped, '/clicked_point', self.callback_clicked_point, 1)
        self.publisher_ = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 1)

    def callback_clicked_point(self, msg):
        self.get_logger().info(f'Points:\n X: {msg.point.x,} \n Y: {msg.point.y} \n Z: {msg.point.z}')
        self.publish_initialpose(msg.point.x, msg.point.y, msg.point.z)

    def publish_initialpose(self, x, y, z):

        msg = PoseWithCovarianceStamped()
        msg.header.frame_id = 'map'
        msg.pose.pose.position.x = x
        msg.pose.pose.position.y = y
        msg.pose.pose.position.z = z 
        msg.pose.pose.orientation.w = 1.0
        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing:\n X = {x}, Y = {y}, W = 1.0')

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
