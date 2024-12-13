import cv2

import numpy as np

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("../bambi.png", flags=cv2.IMREAD_GRAYSCALE)

# 腐蚀
kernel = np.ones((10, 10), np.uint8)
erosion1 = cv2.erode(img, kernel, iterations=1)
erosion2 = cv2.erode(img, kernel, iterations=2)
erosion3 = cv2.erode(img, kernel, iterations=3)

erobin = np.hstack((erosion1, erosion2, erosion3))

# 膨胀
dilate1 = cv2.dilate(img, kernel=kernel, iterations=1)
dilate2 = cv2.dilate(img, kernel=kernel, iterations=2)
dilate3 = cv2.dilate(img, kernel=kernel, iterations=3)

dibin = np.hstack((dilate1, dilate2, dilate3))

bin = np.vstack((erobin, dibin))
show = cv2.resize(bin, (0, 0), fx=0.5, fy=0.5)
cv2.imshow("show", show)
cv2.waitKey(0)
