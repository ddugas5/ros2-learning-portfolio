

import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__('add_two_ints_client')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) != 3:
        print("usage: add_two_ints_client.py X Y")
        return
    
    client = AddTwoIntsClient()
    client.send_request(int(sys.argv[1]), int(sys.argv[2]))

    while rclpy.ok():
        rclpy.spin_once(client)
        if client.future.done():
            try:
                response = client.future.result()
            except Exception as e:
                client.get_logger().info(f'Service call failed: {e}')
            else:
                client.get_logger().info(f'Result: {response.sum}')
            break
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()