#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import time
from sensor_msgs.msg import Image

class pub_webcam(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("我是發佈者哦。")


def main():
    rclpy.init(args=None) #ROS2端口初始化
    node=pub_webcam("topic_pub_webcam") #建立節點
    pub=node.create_publisher(Image, "image_raw", 10)#建立視訊流推送
    cap = cv2.VideoCapture(0)
    brige=CvBridge()
    while True:
        ret, frame = cap.read()
        data = brige.cv2_to_imgmsg(frame, 'bgr8')#cv2轉成np.arrary
        pub.publish(data)#推送到訂閱者端口