import numpy as np
import cv2

# 打开摄像头
camera = cv2.VideoCapture(0)

# 形态学操作
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# 创建混合高斯模型用于背景建模
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = camera.read()

    if not ret:
        print("无法接收帧 (摄像头已断开?)")
        break
    # 应用高斯模型
    fgmask = fgbg.apply(frame)

    # 形态学开运算去噪点
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel=kernel)

    # 寻找视频中的轮廓
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, 
            cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        # 计算各轮廓周长
        perimeter = cv2.arcLength(c, True)
        if perimeter > 1000:
            # 找到一个直矩形（不会旋转）
            x, y, w, h = cv2.boundingRect(c)
            # 画出这个矩形
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,  0, 255), 2)

        elif perimeter > 800:
            # 找到一个直矩形（不会旋转）
            x, y, w, h = cv2.boundingRect(c)
            # 画出这个矩形
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        elif perimeter > 500:
            # 找到一个直矩形（不会旋转）
            x, y, w, h = cv2.boundingRect(c)
            # 画出这个矩形
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    fgmask = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
    show = np.hstack((frame, fgmask))
    cv2.imshow("show", show)
    # cv2.imshow('frame', frame)
    # cv2.imshow('fgmask', fgmask)

    # 按下 'q' 键退出
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
