import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import SetBool


class TurnRight(Node):

    def __init__(self):
        super().__init__('turn_right_service')
        self.service = self.create_service(SetBool, 'turn_right', self.turn_callback)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info('Turn Right Service is ready!')

    def turn_callback(self, request, response):
        twist = Twist()

        if request.data: 
            twist.angular.z = -0.5  
            self.publisher.publish(twist)
            response.message = 'Turning right!'
        else:  
            twist.angular.z = 0.0  
            self.publisher.publish(twist)
            response.message = 'Stopped!'

        return response

def main(args=None):
    rclpy.init(args=args)
    
    
    turn_right_service = TurnRight()

    try:
        rclpy.spin(turn_right_service)
    except KeyboardInterrupt:
        turn_right_service.get_logger().info('Error Turn Right ')
    finally:
        turn_right_service.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
