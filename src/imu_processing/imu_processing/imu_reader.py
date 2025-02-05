#the purpose of this code is to read imu data 
#from an imu topic and print it out

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Imu

class IMUReader(Node):
    def __init__(self):
        super().__init__('imu_reader')
        self.subscription = self.create_subscription(
            Imu,
            'imu_plugin/out',
            self.imu_subscriber_callback,
            10)
        self.subscription

    def imu_subscriber_callback(self, msg):
        self.get_logger().info(
            f"Orientation: x={msg.orientation.x}, y={msg.orientation.y}, z={msg.orientation.w}"
        )

        self.get_logger().info(
            f"Angular Velocity: x={msg.angular_velocity.x}, y={msg.angular_velocity.y}, z={msg.angular_velocity.z}"
        )

        self.get_logger().info(
            f"Linear Velocity: x={msg.linear_acceleration.x}, y={msg.linear_acceleration.y}, z={msg.linear_acceleration.z}"
        )

def main(args=None):
    rclpy.init(args=args)

    imu_reader = IMUReader()

    rclpy.spin(imu_reader)

    imu_reader.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()