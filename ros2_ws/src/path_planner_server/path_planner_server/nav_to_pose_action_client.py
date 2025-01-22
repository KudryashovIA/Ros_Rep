import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient

class NavToPoseActionClient(Node):
    def __init__(self):
        super().__init__('nav_to_pose_action_client')

        # Подписка на /clicked_point
        self.subscription = self.create_subscription(
            PointStamped,
            '/clicked_point',
            self.point_callback,
            10
        )

        # Action Client для /navigate_to_pose
        self.action_client = ActionClient(self, NavigateToPose, '/navigate_to_pose')

        self.get_logger().info('Node is start')

    def point_callback(self, msg):
        # Извлечение координат из PointStamped
        x, y, z = msg.point.x, msg.point.y, msg.point.z
        self.get_logger().info(f'Point: x={x}, y={y}, z={z}')

        # Отправка цели роботу
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = "map"
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.w = 1.0 

        self.action_client.wait_for_server()
        self.action_client.send_goal_async(goal_msg)
        self.get_logger().info('Moving to my goal.')

def main(args=None):
    rclpy.init(args=args)
    node = NavToPoseActionClient()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
