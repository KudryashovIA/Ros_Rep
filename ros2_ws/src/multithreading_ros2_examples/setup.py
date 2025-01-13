from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'multithreading_ros2_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ivan',
    maintainer_email='kia-snz@mail.ru',
    description='TODO: Package description',
    license='TODO: License declaration',
    #tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'multithreading = multithreading_ros2_examples.multithreading:main',
            'multithreading_movement_server_parallel = multithreading_ros2_examples.multithreading_movement_server_parallel:main',
            'multithreading_movement_server_and_calculation_server = multithreading_ros2_examples.multithreading_movement_server_and_calculation_server:main'

        ],
    },
)
