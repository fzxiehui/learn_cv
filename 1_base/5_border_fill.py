import cv2

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

top_size, bottom_size, left_size, right_size = (100, 100, 100, 100)

# 读取图像
img = cv2.imread("../bambi.png")

# 复制法, 最边缘像素向外延展
replicate = cv2.copyMakeBorder(img, 
        top_size, bottom_size, 
        left_size, right_size, borderType=cv2.BORDER_REPLICATE)

# 返射法, 四个方向倒影
reflect = cv2.copyMakeBorder(img,
        top_size, bottom_size, 
        left_size, right_size, borderType=cv2.BORDER_REFLECT)

# 返射法, 四个方向倒影
reflect101 = cv2.copyMakeBorder(img,
        top_size, bottom_size, 
        left_size, right_size, borderType=cv2.BORDER_REFLECT_101)

# 外包装法(包装盒贴图)
wrap = cv2.copyMakeBorder(img,
        top_size, bottom_size, 
        left_size, right_size, borderType=cv2.BORDER_WRAP)

# 常量法, 常数填充
constant = cv2.copyMakeBorder(img,
        top_size, bottom_size, 
        left_size, right_size, borderType=cv2.BORDER_CONSTANT, value=0)

cv2.imshow("replicate", replicate)
cv2.waitKey(0)

cv2.imshow("reflect", reflect)
cv2.waitKey(0)

cv2.imshow("reflect101", reflect101)
cv2.waitKey(0)

cv2.imshow("wrap", wrap)
cv2.waitKey(0)

cv2.imshow("constant", constant)
cv2.waitKey(0)
