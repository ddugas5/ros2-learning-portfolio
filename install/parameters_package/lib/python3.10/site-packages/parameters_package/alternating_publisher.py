import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AlternatingPublisher(Node):
    def __init__(self):
        super().__init__('alternating_publisher')

        #declare parameter for the timer
        self.declare_parameter('timer_interval', 2.0)
        self.timer_interval = self.get_parameter('timer_interval').value

        self.publisher_ = self.create_publisher(String, 'chatter', 10)

        self.timer = self.create_timer(self.timer_interval, self.timer_callback)
        
        self.toggle = True
    
    def timer_callback(self):
        msg = String()

        if self.toggle:
            msg.data = "hello"

        else:
            msg.data = "goodbye"

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing: "{msg.data}"')

        self.toggle = not self.toggle

def main(args=None):
    rclpy.init(args=args)
    alternating_publisher = AlternatingPublisher()
    rclpy.spin(alternating_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()