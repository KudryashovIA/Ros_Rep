import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Exercise21(Node):

    def __init__(self):
        super().__init__('exercise')
        # use the Twist module for /cmd_vel topic
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscriber_ = self.create_subscription(LaserScan, '/scan', self.laser_scan_callback, 10)
        # define the timer period for 0.5 seconds
        timer_period = 0.5
        #self.timer = self.create_timer(timer_period, self.timer_callback)

    def laser_scan_callback(self,msg):

        front_ranges = msg.ranges[345:] + msg.ranges[:15]
        min_distance = min(front_ranges)

        msg = Twist()

        if  min_distance > 1.0:
            msg.linear.x = 0.0
            msg.angular.z = 0.5
        elif min_distance > 0.5:
            msg.linear.x = 0.1
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)

            
def main(args=None):
    rclpy.init(args=args)
    exercise = Exercise21()
    rclpy.spin(exercise)
    exercise.destroy_node() 
    rclpy.shutdown()

if __name__ == '__main__':
    main()