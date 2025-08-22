#!/usr/bin/env python3
import rclpy
import math
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
 
 
class TurtleControllerNode(Node): 
    def __init__(self):
        super().__init__("turtle_controller") 
        self.target_x = 8.0
        self.target_y = 4.0
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
        
        self.control_loop_timer_ =self.create_timer(
            0.01,
            self.control_loop
        )
        
    def callback_pose(self, pose: Pose):
            self.pose_ = pose
            
    def control_loop(self):
            if self.pose_ == None:
                return
            
            dist_x = self.target_x - self.pose_.x
            dist_y = self.target_y - self.pose_.y
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