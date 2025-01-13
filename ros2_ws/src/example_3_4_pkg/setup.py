from setuptools import find_packages, setup

package_name = 'example_3_4_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'mutualexclusive_demo_fun = example_3_4_pkg.callback_groups_examples:mutualexclusive_demo_fun' 
        ],
    },
)
