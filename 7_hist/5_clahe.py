import cv2
import numpy as np

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("../bambi.png", flags=cv2.IMREAD_GRAYSCALE)

equ = cv2.equalizeHist(img)

# 创建直方图均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# 应用于图像
res_clahe = clahe.apply(img)
res = cv2.resize(np.hstack((img, equ, res_clahe)), (0, 0), fx=0.5, fy=0.5)
# 使用 OpenCV 显示图像
cv2.imshow('res', res)
cv2.waitKey(0)

