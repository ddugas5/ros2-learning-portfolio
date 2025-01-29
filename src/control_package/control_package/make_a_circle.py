import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CirclePublisher(Node):
    def __init__(self):
        super().__init__('circle_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
    
    def timer_callback(self):
        twist = Twist()
        twist.linear.x = 0.25
        twist.angular.z = 0.30
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    circle_publisher = CirclePublisher()
    rclpy.spin(circle_publisher)
    circle_publisher.destroy_node
    rclpy.shutdown()

if __name__ == '__main__':
    main()