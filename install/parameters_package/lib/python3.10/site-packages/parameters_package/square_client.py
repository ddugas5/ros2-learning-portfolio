import rclpy
from rclpy.node import Node
from parameters_package.srv import SquareOneInt

class SquareClient(Node):
    def __init__(self):
        super().__init__('square_client')
        self.client = self.create_client(SquareOneInt, 'square_one_int_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')

        self.request = SquareOneInt.Request()

    def send_request(self, a):
        self.request.a = a
        self.future = self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self, self.future)
        if self.future.result() is not None:
            self.get_logger().info(f'Result: {self.future.result().total}')
        else:
            self.get_logger().info('Service call failed.')

def main(args=None):
    rclpy.init(args=args)
    client = SquareClient()
    client.send_request(3)  # Change this number as needed
    rclpy.shutdown()

if __name__ == '__main__':
    main()
