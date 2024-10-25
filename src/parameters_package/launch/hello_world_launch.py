
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('parameters_package'),
        'config',
        'params.yaml'
    )

    return LaunchDescription([
        Node(
            package = 'parameters_package',
            executable = 'hello_world',
            name = 'hello_world_publisher',
            parameters=[config]
        )
    ])