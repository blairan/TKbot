from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    
    map_server = Node(
        package="nav2_map_server",
        executable="map_saver_cli",
        output = "screen",
        arguments=["-f", "src/maps/nav"]
    )
    return LaunchDescription([map_server])