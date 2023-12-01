# tkbot
 my tkbot for ros2
 # 注意事項
  - 檔案分成上位機和下位機,上位機是把src下載到樹莓派端,下位機是upload到arduino mega2560;
  - 下位機的電機PID如果用於另一台,必須要再調整;
  - 下位機的電機減比要注意,可以參考下位機資料夾裡的"注意事項"
  - catographer和slam_gmapping，usb_cam功能包要另外自行下載再編譯;
# 底盤測試
 - 機器人端－終端機
  <pre><code>
   cd tkbot_ws
   . install/setup.bash
   ros2 launch tkbot_integrate tkbot_descript.launch.py
  </code></pre>
 - pc終端機
  <pre>
   <code>
     rviz2 #--1終端
     ros2 run teleop_twist_keyboard teleop_twist_keyboard #2終端
   </code>
  </pre>
 # 手持雷達建圖-catographer
  - 機器人端－#1終端機
   <pre><code>
    cd tkbot_ws
    . install/setup.bash
    ros2 launch tkbot_integrate tkbot_descript.launch.py
   </code></pre>
  - 機器人端－#2終端機
    <pre><code>
     cd tkbot_ws
     . install/setup.bash
     ros2 launch tkbot_cartographer cartographer.launch.py
    </code></pre>
  - pc終端機
    <pre><code>
      ros2 run teleop_twist_keyboard teleop_twist_keyboard
     </code></pre>
  - 建圖好後保存地圖
     <pre><code>
      ros2 run nav2_map_server map_saver_cli -t maps -f nav
     </code></pre>
 # slam_gmapping建圖
  - 機器人端－第一個終端機
    <pre><code>
     cd tkbot_ws
     . install/setup.bash
     ros2 launch tkbot_integrate tkbot_descript.launch.py
    </code></pre>
  - 機器人端－第二個終端機
    <pre><code>
     cd tkbot_ws
     . install/setup.bash
     ros2 launch slam_gmapping slam_gmapping.launch.py
    </code></pre>
  - pc端終端機
    <pre><code>
     ros2 run teleop_twist_keyboard teleop_twist_keyboard
    </code></pre>
  - 建圖好後保存地圖
     <pre><code>
      ros2 run nav2_map_server map_saver_cli -t maps -f nav
     </code></pre>

＃　yolo_ros
 - 機器人端－終端機
   <pre>
    <code>ros2 run yolov5_ros2 yolo_detect_2d --ros-args -p device:=cpu -p image_topic:=/image -p pub_result_img:=True</code>
   </pre>
  
