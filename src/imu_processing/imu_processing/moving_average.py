#the purpose of this code is to read imu data
#from an imu topic and implement a simple filter to smooth imu readings

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Imu
from collections import deque

class IMUFilter(Node):
    def __init__(self):
        super().__init__('imu_filter')
        self.subscription = self.create_subscription(
            Imu,
            'imu_plugin/out',
            self.imu_subscriber_callback,
            10)

        self.publisher = self.create_publisher(Imu, 'imu/filtered', 10)

        self.window_size = 10
        self.ang_vel_x = deque(maxlen=self.window_size)
        self.ang_vel_y = deque(maxlen=self.window_size)
        self.ang_vel_z = deque(maxlen=self.window_size)

    def imu_subscriber_callback(self, msg):
        self.ang_vel_x.append(msg.angular_velocity.x)
        self.ang_vel_y.append(msg.angular_velocity.y)
        self.ang_vel_z.append(msg.angular_velocity.z)

        avg_x = sum(self.ang_vel_x) / len(self.ang_vel_x)
        avg_y = sum(self.ang_vel_y) / len(self.ang_vel_y)
        avg_z = sum(self.ang_vel_z) / len(self.ang_vel_z)

        filtered_msg = Imu()
        filtered_msg.header = msg.header
        filtered_msg.angular_velocity.x = avg_x
        filtered_msg.angular_velocity.y = avg_y
        filtered_msg.angular_velocity.z = avg_z

        self.publisher.publish(filtered_msg)


def main(args=None):
    rclpy.init(args=args)

    imu_filter = IMUFilter()

    rclpy.spin(imu_filter)

    imu_filter.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
