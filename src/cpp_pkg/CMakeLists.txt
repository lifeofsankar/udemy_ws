cmake_minimum_required(VERSION 3.8)
project(cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

add_executable(cpp_node src/first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)

add_executable(robot_news_stat src/robot_ns.cpp)
ament_target_dependencies(robot_news_stat rclcpp example_interfaces)

add_executable(phone src/phone.cpp)
ament_target_dependencies(phone rclcpp example_interfaces)

install(TARGETS
  cpp_node
  robot_news_stat
  phone
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
