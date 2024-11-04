from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Path to URDF file
    urdf_file = os.path.join(
        os.path.expanduser('~'),
        'ros2-learning-portfolio',
        'src',
        'robot_package',
        'urdf',
        'my_mobile_robot.urdf'
    )

    # Load the URDF file
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        )
    ])
