from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    pkg_name = "tkbot_urdf_model"
    urdf_name = "tkbot_model.urdf"
    pkg_share = FindPackageShare(package=pkg_name).find(pkg_name)
    urdf_model = os.path.join(pkg_share, f"urdf/{urdf_name}")

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        arguments=[urdf_model]
    )

    joint_state_publisher = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
    )

    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )

    rviz2 = Node(
        package='rviz2',
        executable="rviz2",
        name = "rviz2"
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        # joint_state_publisher_gui,
        # rviz2,
    ])