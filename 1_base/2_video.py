import cv2
import sys


#!!!!! 最初使用 ~/test.mp4 无法打开视频!!!!!
video_name = "/home/hello/test.mp4"

# 打开视频 如果是设备的话把文件名改为 0 1 2 代表设备编号
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(video_name)

if not cap.isOpened():
    print("open video")
    cap.open(video_name)

print("video open Status: ", cap.isOpened())

if not cap.isOpened():
    print("video open Error!")
    sys.exit(1)

while True:

    ret, frame = cap.read()
    if frame is None:
        break

    if ret == True:
        # 转灰度
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("video", gray)
        cv2.imshow("video", frame)
        # esc 退出
        if cv2.waitKey(10) & 0xFF == 27:
            break

cap.release()

