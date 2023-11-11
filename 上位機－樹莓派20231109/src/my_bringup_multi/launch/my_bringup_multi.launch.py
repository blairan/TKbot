# #封裝終端指令相關類
# from launch.actions import ExecuteProcess
# from launch.substitutions import FindExecutable
#參數聲明與獲取
# from launch.actions import DeclareLaunchArgument
# from launch.substitutions import LaunchConfiguration
#文件包含相關
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
# #分組相關
from launch_ros.actions import PushRosNamespace
from launch.actions import GroupAction
# #事件相關
# from launch.event_handlers import OnProcessStart, OnProcessExit
# from launch.actions import ExecuteProcess, RegisterEventHandler, LogInfo
# #獲取功能包下的目錄
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
import os
from launch_ros.actions import Node

'''
需求分析：
    １.不同機器人的相同模組，要有唯一的坐標系標識；
        例如：odom1 base_footprint1 base_link1 laser1 camera1
             odom2 base_footprint2 base_link2 laser2 camera2
    2.不同機器人要發布相對於map的坐標系關係
        map-->odom1
        map-->odom2
    3.須要為機器人發布訂閱的話題設置命名空間
        /car1/scan
        /car2/scan
實　　現：
    １.每個機器人都須要創建一個針對編隊而實現的功能包；
    ２.在該機器人的功能包中重新設置坐標系名稱，發布里程計相對於map的坐標變換，
    　並為當前機器人節點設定命名空間
'''

def generate_launch_description():
    #１.啟動機器人的各個模組(不要包含之前功能包提供的launch文件，而是要直接調用節點
    # 並為之設計新的節點)
    base_driver = Node(
                package="ros2_arduino_bridge", 
                executable="arduino_node", 
                name="ros2_arduino_node",
                parameters=[os.path.join(get_package_share_directory("my_bringup_multi"),"params","arduino.yaml")],
            )
    laser_launch = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource(
            launch_file_path=os.path.join(
                get_package_share_directory('lslidar_driver'),
                                'launch',
                                'lsn10_launch.py'
            )
        ),launch_arguments=[
            ('frame_id', 'laser1')
        ]
    )

    #相機
    camera_node = Node(
                package='usb_cam', executable='usb_cam_node_exe', output='screen',
                name="camera_node",
                arguments=[os.path.join(get_package_share_directory('my_bringup_multi'),'params','params.yaml')]
            )
    
    #2.以分組的方式為當前的機器人各個模組設置相同的命名空間
    group = GroupAction([PushRosNamespace('car1'), base_driver, laser_launch, camera_node])
    
    #3.發布坐標變換
    odom2map = Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            arguments=["--x", "0.3", "--y", "-0.4", "--frame-id", "map", "--child-frame-id", "odom1"]
        )
    
    baselink2base_footprint = Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            arguments=["--z", "-0.05", "--frame-id", "base_footprint1", "--child-frame-id", "base_link1"]
        )
    
    laser2base_link = Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            arguments=["--z", "-0.07", "--frame-id", "base_link1", "--child-frame-id", "laser1"],
        )
    
    tf2camera = Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            arguments=["--x", "-0.15", "--z", "0.05", "--frame-id", "base_link1", "--child-frame-id", "camera1"]
        )
    return LaunchDescription([group, odom2map, tf2camera, baselink2base_footprint, laser2base_link])