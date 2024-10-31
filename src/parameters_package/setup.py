from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'parameters_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'srv'), glob('srv/*.srv')),  # Correct way to reference srv files
      
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='davey',
    maintainer_email='ddugashf1@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_world = parameters_package.hello_world:main',
            'square_client = parameters_package.square_client:main',
            'square_service = parameters_package.square_service:main',
            'alternating_publisher = parameters_package.alternating_publisher:main',
        ],
    },
)
