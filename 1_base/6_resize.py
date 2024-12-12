import cv2

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("../bambi.png")

# 放大1.5 倍
res = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)
cv2.imshow("1.5", res)
cv2.waitKey(0)

# w = 1300 h = 800
# !!!反常识, 这里用的是 w, h shape 用的是 h, w
res = cv2.resize(img, (1300, 800))
cv2.imshow("1.5", res)
cv2.waitKey(0)

