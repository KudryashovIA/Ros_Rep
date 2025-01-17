from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'exercise31_pkg'

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
            'exercise31 = exercise31_pkg.exercise31:main',
            'exercise32 = exercise31_pkg.exercise32:main',
            'exercise33 = exercise31_pkg.exercise32:main',
        ],
    },
)
