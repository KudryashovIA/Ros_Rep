import rclpy
# import the ROS2 python libraries
from rclpy.node import Node
# import the LaserScan module from sensor_msgs interface
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
# import Quality of Service library, to set the correct profile and reliability in order to read sensor data.
from rclpy.qos import ReliabilityPolicy, QoSProfile


class SimpleRemapper(Node):

    def __init__(self):

        super().__init__('simple_remapper')
        
        # We wait for the topic to be ready before taing any action
        self.subscriber_topic_ready = False
        # Create susbcriber publisher
        self.subscriber= self.create_subscription(
            LaserScan,
            '/in_my_scan',
            self.listener_callback,
            QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT))

        # prevent unused variable warning
        self.subscriber
        # define the variable to save the received info
        self.laser_left = 0
        self.laser_right = 0
        self.laser_forward = 0
        

        # create the publisher object
        self.publisher_ = self.create_publisher(Twist, '/out_cmd_vel', 10)

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def listener_callback(self, msg):
        # print the log info in the terminal
        self.update_laser_data(msg)
        self.get_logger().debug('LASER VALUE: "%s"' % str(self.laser_forward))
        self.subscriber_topic_ready = True
    
    def update_laser_data(self, laser_data):

        length_scan_data = len(laser_data.ranges)
        left_index = int(length_scan_data / 4)
        center_index = int(length_scan_data / 2)
        right_index = int(3 * (length_scan_data / 4))

        self.get_logger().info("left_index = "+str(left_index))
        self.get_logger().info("center_index = "+str(center_index))
        self.get_logger().info("right_index = "+str(right_index))

        self.laser_left = laser_data.ranges[left_index]
        self.laser_right = laser_data.ranges[right_index]
        self.laser_forward = laser_data.ranges[center_index]

        self.get_logger().info("LEFT = "+str(self.laser_left))
        self.get_logger().info("FORWARDS = "+str(self.laser_forward))
        self.get_logger().info("RIGHT = "+str(self.laser_right))
        


    def timer_callback(self):
        # Here we have the callback method
        # create a Twist message
        msg = Twist()
        if self.subscriber_topic_ready:
            if self.laser_forward <= 1.0 or self.laser_right <= 1.0:            
                msg.angular.z = 0.5
                msg.linear.x = 0.0
                self.get_logger().info("LEFT because "+str(self.laser_forward)+" <= 0.5, OR "+str(self.laser_right)+" <= 0.5")
            elif self.laser_left <= 1.0:  
                msg.angular.z = -0.5
                msg.linear.x = 0.0
                self.get_logger().info("RIGHT because "+str(self.laser_left)+" <= 0.5")
            else:
                msg.angular.z = 0.0
                msg.linear.x = 0.5
                self.get_logger().info("FORWARDS because "+str(self.laser_forward)+" <= 0.5")

            # Publish the message to the topic
            self.publisher_.publish(msg)
            # Display the message on the console
        
        else:
            self.get_logger().error("Topic /in_my_scan not ready yet..."+str(self.subscriber_topic_ready))
            
def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor
    simple_remapper = SimpleRemapper()
    # pause the program execution, waits for a request to kill the node (ctrl+c)
    rclpy.spin(simple_remapper)
    # Explicity destroy the node
    simple_remapper.destroy_node()
    # shutdown the ROS communication
    rclpy.shutdown()

if __name__ == '__main__':
    main()