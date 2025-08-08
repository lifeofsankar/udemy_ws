from setuptools import find_packages, setup

package_name = 'py_pkg'

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
    maintainer='admin',
    maintainer_email='jaisankar@asimovtrainees.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = py_pkg.first_node:main",
            "robot_news_stat = py_pkg.robot_ns:main",
            "phone = py_pkg.phone:main",
            "number_publisher = py_pkg.number_publisher:main",
            "number_counter = py_pkg.number_counter:main",
            "add_twp_ints_server = py_pkg.add_two_ints_server:main",
            "add_two_ints_client_no_oop = py_pkg.add_two_ints_client_no_oop:main",
            "add_two_ints_client = py_pkg.add_two_ints_client:main"
        ],
    },
)
