# tkbot
 my tkbot for ros2
 # 注意事項
  - 檔案分成上位機和下位機,上位機是把src下載到樹莓派端,下位機是upload到arduino mega2560;
  - 下位機的電機PID如果用於另一台,必須要再調整;
  - 下位機的電機減比要注意,可以參考下位機資料夾裡的"注意事項"
  - catographer和slam_gmapping，usb_cam功能包要另外自行下載再編譯;
# 底盤測試
  <pre><code>
   $ cd tkbot_ws
   $ . install/setup.bash
   $ ros2 launch tkbot_integrate tkbot_descript.launch.py
 </code></pre>
