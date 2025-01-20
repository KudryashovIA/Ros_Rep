import rclpy
from rclpy.node import Node
from rcl_interfaces.srv import SetParameters
from rcl_interfaces.msg import Parameter, ParameterType

class ClientParam(Node):

    def __init__(self):
        super().__init__('client_param')
        self.client = self.create_client(SetParameters, 'amcl/set_parameters')

    def send_request(self):
        request = SetParameters.Request()

        alpha1 = Parameter()
        alpha1.name = 'alpha1'
        alpha1.value.type = ParameterType.PARAMETER_DOUBLE
        alpha1.value.double_value = 0.3

        alpha2 = Parameter()
        alpha2.name = 'alpha2'
        alpha2.value.type = ParameterType.PARAMETER_DOUBLE
        alpha2.value.double_value = 0.15

        request.parameters = [alpha1, alpha2]

        future = self.client.call_async(request)
        return future


def main(args=None):
    rclpy.init(args=args)
    client = ClientParam()
    future = client.send_request()

    rclpy.spin_until_future_complete(client, future)

    if future.result() is not None:
        client.get_logger().info('Successfull changed')
    else:
        client.get_logger().error('Failed')

    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
