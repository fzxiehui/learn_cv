import cv2

import numpy as np

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("../bambi.png", flags=cv2.IMREAD_GRAYSCALE)


sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# 白到黑是整数， 黑到白是负数， 所有的负数会被截断成0， 所以要取绝对值
sobelx = cv2.convertScaleAbs(sobelx)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobelx)


# 合并x,y
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)


bin = np.hstack((img, sobelx, sobely, sobelxy))
show = cv2.resize(bin, (0, 0), fx=0.5, fy=0.5)

cv2.imshow("show", show)
cv2.waitKey(0)
