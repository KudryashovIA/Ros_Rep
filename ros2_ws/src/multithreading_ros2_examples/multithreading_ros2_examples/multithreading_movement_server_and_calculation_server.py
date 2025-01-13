import rclpy
from rclpy.node import Node
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from std_srvs.srv import SetBool
from geometry_msgs.msg import Twist
import time
from sensor_msgs.msg import LaserScan
from rclpy.callback_groups import ReentrantCallbackGroup

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

        start_time = time.time()
        self.get_logger().info(f'Sleep for 15 seconds start at:{time.strftime("%H:%M:%S", time.localtime(start_time))})')

        time.sleep(15.0)

        end_time = time.time()
        self.get_logger().info(f'Done sleeping at: {time.strftime("%H:%M:%S", time.localtime(end_time))}')


        return response


class CalculationsServiceServer(Node):

    def __init__(self):
        super().__init__('calculations_service_server')
    
        self.calculation_group = MutuallyExclusiveCallbackGroup()
        self.reentrant_group = ReentrantCallbackGroup()
  

        self.crv = self.create_service(SetBool, '/calculations',self.Calculations_callback, callback_group = self.calculation_group)

        self.subscriber_ = self.create_subscription(LaserScan, '/scan', self.Laser_callback, 10, callback_group = self.reentrant_group)
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        self.laser_value = None

    

    def Calculations_callback(self, request, response):

        if request.data:

            laser_value1 = self.laser_value
            self.get_logger().info(f'Start scan')
            time.sleep(5.0)

            laser_value2 = self.laser_value
            delta = laser_value2 - laser_value1

            self.get_logger().info(f'Delta: {delta}')
        
            cmd = Twist()

            if delta > 0:
                cmd.linear.x = 0.5
                self.get_logger().info('Moving straight')

            elif delta < 0:
                cmd.linear.x = -0.5
                self.get_logger().info('Moving back')
            else:
                cmd.linear.x = 0.0 
                self.get_logger().info('Stop')

            self.publisher_.publish(cmd)
            self.get_logger().info(f'Publish cmd: linear.x = {cmd.linear.x}, angular.z = {cmd.angular.z}')
    
            response.success = True
            response.message = "Calculations completed successfully."

        return response
    
    def Laser_callback(self, msg):
        self.laser_value = msg.ranges[359]
    


def main(args=None):
    rclpy.init(args=args)

    service_server = ServiceServer()
    calculations_service_server = CalculationsServiceServer()
    
    executor = MultiThreadedExecutor(num_threads=8)  
    executor.add_node(service_server)
    executor.add_node(calculations_service_server)

    try:
        executor.spin()
    finally:
        service_server.destroy_node()
        calculations_service_server.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

#ros2 service call /start_turn std_srvs/srv/SetBool "{data: false}"
#ros2 service call /calculations std_srvs/srv/SetBool "{data: true}"    
    