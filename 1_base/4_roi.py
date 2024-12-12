import cv2

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 读取图像
img = cv2.imread("../bambi.png")

"""
    区域选定
"""
# h,w
area = img[50:500, 150:600]

cv2.imshow("area", area)
cv2.waitKey(0)


"""
    获取单通道
"""
b, g, r = cv2.split(img)

cv2.imshow("show b", b)
cv2.waitKey(0)

cv2.imshow("show g", g)
cv2.waitKey(0)

cv2.imshow("show r", r)
cv2.waitKey(0)


"""
    通道合并
"""

merge_image = cv2.merge((g, r, b)) # 如果想变回原图 = b,g,r
cv2.imshow("Merge Image ", merge_image)
cv2.waitKey(0)


"""
    数组操作
"""

cur_img = img.copy()

cur_img[:, :, 0] = 0 # B 全设置为0
cur_img[:, :, 1] = 0 # G 全设置为0
# cur_img[:, :, 2] = 0 # R
cv2.imshow("R", cur_img)
cv2.waitKey(0)
