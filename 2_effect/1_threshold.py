import cv2

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread("../bambi.png", flags=cv2.IMREAD_GRAYSCALE)

# 返回值: 阈值, 返回图像
# src: 输入的图像
# thresh:  阈值
# maxval: 最大值
# type: 类型
# - cv2.THRESH_BINARY = 超过 thresh = maxval, 否则 = 0
# - cv2.THRESH_BINARY_INV 与 cv2.THRESH_BINARY 相反
# - cv2.THRESH_TRUNC 大于阈值设为阈值，否则不变
# - cv2.THRESH_TOZERO 大于阈值不变，否则设置为0
# - cv2.THRESH_TOZERO_INV 与 cv2.THRESH_TOZERO 相反
ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, binary_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, trunc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, tozero = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, tozero_inv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("BINARY", binary)
cv2.waitKey(0)

cv2.imshow("BINARY_INV", binary_inv)
cv2.waitKey(0)

cv2.imshow("TRUNC", trunc)
cv2.waitKey(0)

cv2.imshow("TOZERO", tozero)
cv2.waitKey(0)

cv2.imshow("TOZERO_INV", tozero_inv)
cv2.waitKey(0)
