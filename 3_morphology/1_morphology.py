import cv2

import numpy as np

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("../bambi.png", flags=cv2.IMREAD_GRAYSCALE)

# 开运算: 先腐蚀 再膨胀
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(img, 
        cv2.MORPH_OPEN,  # 开运算
        kernel=kernel)

# 闭运算: 先膨胀 再腐蚀

closing = cv2.morphologyEx(img, 
        cv2.MORPH_CLOSE,  # 闭运算
        kernel=kernel)

# 原图， 开， 闭
open_clos_show = np.hstack((img, opening, closing))

# 梯度运算
# 梯度 = 膨胀 - 腐蚀
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# 礼帽黑帽

# 礼帽 = 原始输入 - 开运算结果
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# 黑帽 = 闭运算结果 - 原始输入
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


# 梯度， 礼帽， 黑帽
gtb_show = np.hstack((gradient, tophat, blackhat))

bin = np.vstack((open_clos_show, gtb_show))
show = cv2.resize(bin, (0, 0), fx=0.5, fy=0.5)

cv2.imshow("show", show)
cv2.waitKey(0)
