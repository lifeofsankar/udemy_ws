#include "rclcpp/rclcpp.hpp"
#include "our_robot_interfaces/msg/hardware_status.hpp"
 
using namespace std::chrono_literals;

class HWSPubNode : public rclcpp::Node 
{
public: 
    HWSPubNode() : Node("hardware_status_publisher")
    {
        pub_ = this->create_publisher<our_robot_interfaces::msg::HardwareStatus>(
            "hardware_status", 10);
        timer_ = this->create_wall_timer(
            1s,
            std::bind(&HWSPubNode::publishHWStatus, this));
        RCLCPP_INFO(this->get_logger(),"Hardware status publisher has been started");
    }
 
private:
    void publishHWStatus()
    {
        auto msg = our_robot_interfaces::msg::HardwareStatus();
        msg.temperature = 57.2;
        msg.are_motors_ready = false;
        msg.debug_message = "Motors are too hot";
        pub_->publish(msg);
    }
    rclcpp::Publisher<our_robot_interfaces::msg::HardwareStatus>::SharedPtr pub_;
    rclcpp::TimerBase::SharedPtr timer_;
};
 
int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<HWSPubNode>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}