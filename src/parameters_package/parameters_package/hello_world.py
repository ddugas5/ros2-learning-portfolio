import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloWorldPublisher(Node):
    def __init__(self):    
        super(). __init__('hello_world_publisher')

        self.publisher = self.create_publisher(String, '/my_topic', 10)

        self.declare_parameter('publish_frequency', 10) #1 is the default value
        self.publish_frequency = self.get_parameter('publish_frequency').value
        
        self.timer = self.create_timer(self.publish_frequency, self.hello_publisher)

    def hello_publisher(self):
        msg = String()
        msg.data = 'Hello World'
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    hello_world_publisher = HelloWorldPublisher()
    rclpy.spin(hello_world_publisher)
    hello_world_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
