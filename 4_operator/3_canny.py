import cv2

import numpy as np

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("../bambi.png", flags=cv2.IMREAD_GRAYSCALE)

# 更少细节
big = cv2.Canny(img, 120, 250)
# 更多细节
bit = cv2.Canny(img, 100, 150)

res = np.hstack((big, bit))
cv2.imshow("res", res)
cv2.waitKey(0)
