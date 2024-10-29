from typing import Callable
from rcl_interfaces.msg import SetParametersResult
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.parameter import Parameter
from rcl_interfaces.msg import SetParametersResult


class HelloWorldPublisher(Node):
    def __init__(self):    
        super(). __init__('hello_world_publisher')

        self.publisher = self.create_publisher(String, '/my_topic', 10) #create a publisher

        self.declare_parameter('publish_frequency', 10) #declaring a parameter, 10 is the default value
        self.publish_frequency = self.get_parameter('publish_frequency').value #creating variable publish_frequency and attaching value to it
        
        self.timer = self.create_timer(1.0 / self.publish_frequency, self.hello_publisher) #create timer with initial freq
    
        self.add_on_set_parameters_callback(self.parameter_callback) #register parameter callback

    def parameter_callback(self, params):
        for param in params:
            if param.name == 'publish_frequency' and param.type_ == Parameter.Type.INTEGER:
                self.publish_frequency = param.value

                self.timer.cancel()
                self.timer = self.create_timer(1.0 / self.publish_frequency, self.hello_publisher)
                self.get_logger().info(f'Updated publish frequency to: {self.publish_frequency}')
        return SetParametersResult(successful=True)

    def hello_publisher(self):
        msg = String()
        msg.data = 'Hello World'
        self.publisher.publish(msg)
        #self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    hello_world_publisher = HelloWorldPublisher()
    rclpy.spin(hello_world_publisher)
    hello_world_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()