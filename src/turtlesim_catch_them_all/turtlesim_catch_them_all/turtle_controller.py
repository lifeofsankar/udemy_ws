#!/usr/bin/env python3
import rclpy
import math
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from our_robot_interfaces.msg import Turtle
from our_robot_interfaces.msg import TurtleArray
 
 
class TurtleControllerNode(Node): 
    def __init__(self):
        super().__init__("turtle_controller") 
        self.turtle_to_catch_: Turtle = None
        self.pose_: Pose = None
        
        self.cmd_vel_publisher_=self.create_publisher(
            Twist,
            "/turtle1/cmd_vel",
            10
        )
        
        self.pose_subscriber_=self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.callback_pose,
            10
        )
        
        self.alive_turtles_subscriber_ =self.create_subscription(
            TurtleArray,
            "alive_turtles",
            self.callback_alive_turtles,
            10
        )
        
        self.control_loop_timer_ =self.create_timer(
            0.01,
            self.control_loop
        )
        
    def callback_pose(self, pose: Pose):
            self.pose_ = pose
            
    def callback_alive_turtles(self, msg: TurtleArray):
        if len(msg.turtles) > 0:
            self.turtle_to_catch_ = msg.turtles[0]
        
    
    def control_loop(self):
            if self.pose_ == None or self.turtle_to_catch_ == None:
                return
            
            dist_x = self.turtle_to_catch_.x - self.pose_.x
            dist_y = self.turtle_to_catch_.y - self.pose_.y
            distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)
            
            cmd = Twist()
            
            if distance > 0.5:
                # position
                cmd.linear.x = 2 * distance
                
                # orientation
                goal_theta = math.atan2(dist_y,dist_x)
                diff = goal_theta - self.pose_.theta
                if diff > math.pi:
                    diff -= 2 * math.pi
                elif diff < -math.pi:
                    diff += 2 * math.pi
                cmd.angular.z = 6 * diff
            else:
                #target reached
                cmd.linear.x = 0.0
                cmd.angular.z = 0.0
            
            self.cmd_vel_publisher_.publish(cmd)
 
 
def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()