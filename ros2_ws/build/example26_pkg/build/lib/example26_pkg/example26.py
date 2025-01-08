import rclpy
# import the ROS2 python dependencies
from rclpy.node import Node
from custom_interfaces.msg import Age
import random

class Example26(Node):

    def __init__(self):
        # Here we have the class constructor
        # call the class constructor
        super().__init__('example26')
        # create the publisher object
        self.publisher_ = self.create_publisher(Age, '/robot_age', 1)
        # define the timer period for 0.5 seconds
        self.timer_period = 0.5
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.age = Age()

        

    def timer_callback(self):
        self.age.years = 2021.0
        self.age.months = 5.0
        self.age.days = float(random.randint(0,31))
        self.get_logger().info("Age==>:["+str(self.age)+"]")

        self.publisher_.publish(self.age)

def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor
    example26 = Example26()
    rclpy.spin(example26)
    example26.destroy_node()
    # shutdown the ROS communication
    rclpy.shutdown()

if __name__ == '__main__':
    main()