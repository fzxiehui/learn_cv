import cv2
import sys

camera_name = 0

cap = cv2.VideoCapture(camera_name)

if not cap.isOpened():
    print("open camera")
    cap.open(camera_name)

print("Camera open Status: ", cap.isOpened())

if not cap.isOpened():
    print("Camera open Error!")
    sys.exit(1)

# 获取视频的宽度和高度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frame_width, frame_height)
print("获取分辨率:", frame_size)

fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

# cv2.VideoWriter_fourcc('I','4','2','0') 未压缩的YUV颜色编码格式， \
#    色度子采样为4：2：0，该编码格式具有较好的兼容性，但生成的视频文件较大，文件扩展名为.avi
# cv2.VideoWriter_fourcc('P','I','M','I')MPEG-1编码格式，生成的文件扩展名为.avic
# v2.VideoWriter_fourcc('X','V','I','D')MPEG-4编码格式，如果希望得到的视频大小为平均值，\
#           可以选用这个参数组合。文件扩展名为.avi
# cv2.VideoWriter_fourcc('T','H','E','O')Ogg Vorbis编码格式，文件扩展名为.ogv
# cv2.VideoWriter_fourcc('F','L','V','I')Flash视频格式，文件扩展名为.flv
# cv2.VideoWriter_fourcc('M','P','4','V')文件扩展名.mp4

fourcc = cv2.VideoWriter_fourcc("M", "P", "4", "V")

# 录像保存
out = cv2.VideoWriter("/home/hello/temp/test2.mp4", 
        fourcc, fps, frameSize=frame_size,isColor=True)


while True:

    ret, frame = cap.read()
    if frame is None:
        break

    if ret == True:
        # 转灰度
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("video", gray)
        out.write(frame)
        cv2.imshow("video", frame)
        # esc 退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()

