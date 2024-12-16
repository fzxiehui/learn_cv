import cv2

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 读取图像
img = cv2.imread("../bambi.png")

# 上采 变大
up = cv2.pyrUp(img)
cv2.imshow("up", up)
cv2.waitKey(0)

# 下采 变小
down = cv2.pyrDown(img)
cv2.imshow("down", down)
cv2.waitKey(0)
