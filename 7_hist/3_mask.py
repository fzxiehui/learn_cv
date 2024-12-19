import cv2
import matplotlib.pyplot as plt

import numpy as np

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("../bambi.png", flags=cv2.IMREAD_GRAYSCALE)

# 创建掩码
print("图像高宽:", img.shape[:2])
mask = np.zeros(img.shape[:2], np.uint8)
# 中间填白
mask[100:600, 100:600] = 255
cv2.imshow("mask", mask)
cv2.waitKey(0)
# 图像与操作
masked_img = cv2.bitwise_and(img, img, mask=mask) 
cv2.imshow("masked_img", masked_img)
cv2.waitKey(0)

hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])
plt.plot(hist_mask)

# 保存到内存缓冲区
from io import BytesIO
buf = BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)

# 将缓冲区中的 PNG 转换为 OpenCV 图像
img_array = np.frombuffer(buf.getvalue(), dtype=np.uint8)
hist_img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
buf.close()

# 使用 OpenCV 显示图像
cv2.imshow('Histogram', hist_img)
cv2.waitKey(0)
