cmake_minimum_required(VERSION 3.8)
project(cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(our_robot_interfaces REQUIRED)

add_executable(cpp_node src/first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)

add_executable(robot_news_stat src/robot_ns.cpp)
ament_target_dependencies(robot_news_stat rclcpp example_interfaces)

add_executable(phone src/phone.cpp)
ament_target_dependencies(phone rclcpp example_interfaces)

add_executable(add_two_ints_server src/add_two_ints_server.cpp)
ament_target_dependencies(add_two_ints_server rclcpp example_interfaces)

add_executable(add_two_ints_client_no_oop src/add_two_ints_client_no_oop.cpp)
ament_target_dependencies(add_two_ints_client_no_oop rclcpp example_interfaces)

add_executable(add_two_ints_client src/add_two_ints_client.cpp)
ament_target_dependencies(add_two_ints_client rclcpp example_interfaces)

install(TARGETS
  cpp_node
  robot_news_stat
  phone
  add_two_ints_server
  add_two_ints_client_no_oop
  add_two_ints_client
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
