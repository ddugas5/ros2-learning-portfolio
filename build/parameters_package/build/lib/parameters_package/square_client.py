import sys
import rclpy
from rclpy.node import Node

class SquareOneIntClient(Node):
    def __init__(self):
        super().__init__('square_one_int_client')
        self.cli = self.create_client(SquareOneIntClient, 'square_one_int_client')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        
        self.req = SquareOneIntClient.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.future = self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    client = SquareOneIntClient()
    client.send_request(int(sys.argv[1]))

    while rclpy.ok():
        rclpy.spin_once(client)
        if client.future.done():
            try:
                response = client.future.result()
            except Exception as e:
                client.get_logger().info(f'Service call failed: {e}')
            else:
                client.get_logger().info(f'Result: {response.total}')
            break
    rclpy.shutdown()

if __name__ == '__main__':
    main()