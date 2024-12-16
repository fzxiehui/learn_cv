import cv2

# 打开摄像头
cap = cv2.VideoCapture(0)

# 检查摄像头是否打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 设置分辨率
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # 设置宽度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  # 设置高度

# 获取实际设置的分辨率
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"分辨率: {width}x{height}")

while True:
    # 读取帧
    ret, frame = cap.read()
    if not ret:
        print("无法接收帧 (摄像头已断开?)")
        break

    # 显示帧
    cv2.imshow('frame', frame)

    # 按下 'q' 键退出
    if cv2.waitKey(1) == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
