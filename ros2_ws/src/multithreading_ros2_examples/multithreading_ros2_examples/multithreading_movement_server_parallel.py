import rclpy
from rclpy.node import Node
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from std_srvs.srv import SetBool
from geometry_msgs.msg import Twist
import time

class ServiceServer(Node):

    def __init__(self):
        super().__init__('service_server')
    
        self.setBool_group = MutuallyExclusiveCallbackGroup()
        self.publish_group = MutuallyExclusiveCallbackGroup()
        

        self.crv = self.create_service(SetBool, '/start_turn',self.SetBool_callback, callback_group = self.setBool_group)
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.publish_cmd, callback_group = self.publish_group)
        self.cmd = Twist()
    
    def publish_cmd(self):
        self.publisher_.publish(self.cmd)
        self.get_logger().info(f'Publish cmd: linear.x = {self.cmd.linear.x}, angular.z = {self.cmd.angular.z}')
    
    def SetBool_callback(self, request, response):
        if request.data:
            self.cmd.angular.z = 0.5
            self.cmd.linear.x = 0.0
        else:
            self.cmd.angular.z = 0.0
            self.cmd.linear.x = 0.5

        #self.publisher_.publish(self.cmd)

        start_time = time.time()
        self.get_logger().info(f'Sleep for 15 seconds start at:{time.strftime("%H:%M:%S", time.localtime(start_time))})')

        time.sleep(15.0)

        end_time = time.time()
        self.get_logger().info(f'Done sleeping at: {time.strftime("%H:%M:%S", time.localtime(end_time))}')


        return response

def main(args=None):
    rclpy.init(args=args)

    node = ServiceServer()
    executor = MultiThreadedExecutor(num_threads=2)  
    executor.add_node(node)

    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

#ros2 service call /start_turn std_srvs/srv/SetBool "{data: false}"

    