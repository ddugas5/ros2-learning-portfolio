#the purpose of this code is to read imu data
#and convert the quaternion into euler angles

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Imu
from tf_transformations import euler_from_quaternion

class EulerAngles(Node):
    def __init__(self):
        super().__init__('euler_angles')
        self.imu_subscriber = self.create_subscription(
            Imu,
            'imu_plugin/out',
            self.imu_subscriber_callback,
            10)
        self.imu_subscriber

    def imu_subscriber_callback(self, msg):
        quaternion = (
            msg.orientation.x,
            msg.orientation.y,
            msg.orientation.z,
            msg.orientation.w
        )
        roll, pitch, yaw = euler_from_quaternion(quaternion)

        self.get_logger().info(f"Roll: {roll:.3f}, Pitch: {pitch:.3f}, Yaw: {yaw:.3f}")

def main(args=None):
    rclpy.init(args=args)

    euler_angles = EulerAngles()

    rclpy.spin(euler_angles)

    euler_angles.destroy_node

    rclpy.shutdown()

if __name__ == '__main__':
    main()