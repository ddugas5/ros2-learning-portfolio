import rclpy
from rclpy.node import Node
from parameters_package.srv import SquareOneInt

class SquareOneIntService(Node):
    def __init__(self):
        super().__init__('square_one_int_service')
        self.srv = self.create_service(SquareOneInt, 'square_one_int_service', self.square_one_int_callback)

        self.declare_parameter('scale_factor', 10)
        self.scale_factor = self.get_parameter('scale_factor').value

    def square_one_int_callback(self, request, response):
        result = request.a * request.a
        self.scale_factor = self.get_parameter('scale_factor').value
        response.total = result * self.scale_factor
        self.get_logger().info(f'The square is: {response.total}')
        return response

def main(args=None):
    rclpy.init(args=args)
    service = SquareOneIntService()
    rclpy.spin(service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
