from setuptools import find_packages, setup

package_name = 'basic_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='davey',
    maintainer_email='biscuits_n_davey@tamu.edu',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'basic_publisher = basic_package.basic_publisher:main',
            'basic_subscriber = basic_package.basic_subscriber:main',
            'basic_service = basic_package.basic_service:main',
            'basic_client = basic_package.basic_client:main',
            'fibonacci_action_server = basic_package.fibonacci_action_server:main',
            'fibonacci_action_client = basic_package.fibonacci_action_client:main',
        ],
    },
)
