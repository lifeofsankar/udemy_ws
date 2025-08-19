#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from our_robot_interfaces.msg import LedStateArray
 
class LEDPanelNode(Node): 
    def __init__(self):
        super().__init__("led_panel")
        self.led_states_ = [0,0,0]
        self.led_states_pub_ = self.create_publisher(
            LedStateArray, 
            "led_panel_state", 
            10
        )
        self.led_states_timer_ = self.create_timer(
            5.0,
            self.publish_led_states
        )
        self.get_logger().info("LED Panel node has been started.")
        
    def publish_led_states(self):
        msg = LedStateArray()
        msg.led_states = self.led_states_
        self.led_states_pub_.publish(msg)
 
def main(args=None):
    rclpy.init(args=args)
    node = LEDPanelNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()