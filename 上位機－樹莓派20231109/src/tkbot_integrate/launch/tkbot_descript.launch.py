from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os

def generate_launch_description():

    #獲取機器人模型路徑
    tkbot_model_path = os.path.expanduser("~/tkbot_ws/src/tkbot_urdf_model")
    tkbot_model_file = os.path.join(tkbot_model_path, 'launch', 'display_model.launch.py')


    #獲取ros2_arduino_bridge功能包的路徑
    ros2_arduino_bridge_path = os.path.expanduser("~/tkbot_ws/src/ros2_arduino_bridge")
    ros2_arduino_bridge_file = os.path.join(ros2_arduino_bridge_path, 'launch', 'ros2_arduino.launch.py')

    #獲取激光雷達功能包路徑
    laser_path = os.path.expanduser("/home/blairan_pi/tkbot_ws/src/LSLIDAR_N10_ROS2/src/lslidar_driver")
    laser_file = os.path.join(laser_path, 'launch', 'lsn10_launch.py')

    camera_action = Node(
        package='usb_cam',
        executable='usb_cam_node_exe',
        arguments=["--ros-args", "--params-file", "/home/blairan_pi/tkbot_ws/src/usb_cam_action/usb_cam/config/params_1.yaml"]
    )
    
    #如果不使用小車模型時，tf_pub_base_link，tf_pub_laser必須發布
    tf_pub_base_link = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['--z', '0.05', '--frame-id', 'base_footprint', '--child-frame-id', 'base_link']
    )

    tf_pub_laser = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['--z', '0.12', '--frame-id', 'base_link', '--child-frame-id', 'laser']
    )


    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                tkbot_model_file,
                
            ]),
        ),
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                laser_file,
            ]),
        ),
       
        # tf_pub_base_link,
        # tf_pub_laser,

        #ros2_arduino_bridge放在最後啟動，避免出錯
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                ros2_arduino_bridge_file,
            ])
        ),

        camera_action,
    ])