import cv2
import numpy as np

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("../bambi.png", flags=cv2.IMREAD_COLOR)

# 均值滤波
blur = cv2.blur(img, # 图像
        (5, 5)) # 均值矩阵大小

# 方框滤波
# 基本和均值滤波一样，可选归一化, normalize
box = cv2.boxFilter(img, -1, (3, 3), normalize=True)

# 这个就是累加超过255的，就都取255, 就是会保留极暗部分
box2 = cv2.boxFilter(img, -1, (2, 2), normalize=False)

# 拼图显示 横向
res = np.hstack((blur, box, box2))
cv2.imshow("blur & box", res)
cv2.waitKey(0)

# 高斯滤波、平划处理、正态分布
aussian = cv2.GaussianBlur(img, (5, 5), 1)

# 中值滤波(中值代替)
median = cv2.medianBlur(img, 5)

# 拼图显示 纵向
# res = np.vstack((aussian, median))
res = np.hstack((aussian, median))
cv2.imshow("aussian & median", res)
cv2.waitKey(0)
