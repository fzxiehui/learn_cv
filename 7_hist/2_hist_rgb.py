import cv2
import matplotlib.pyplot as plt

import numpy as np

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("../bambi.png")

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

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
