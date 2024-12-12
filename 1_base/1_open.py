import cv2

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# 读取图像
img = cv2.imread("../bambi_temp.png")

print(img.shape)
# (736, 736, 3) -> (h, w, c)
# c = 图像类型 正常有 3, 4, 
# 无 无代表为灰度图 cv2.IMREAD_GRAYSCALE 
# 3 代表BGR cv2.IMREAD_COLOR
# 4 代表BGRA cv2.IMREAD_UNCHANGED

# 图像类型
print(type(img))
# <class 'numpy.ndarray'>

# 图像大小
print(img.size)
# 433008

# 图像数据类型
print(img.dtype)
# uint8

# 显示图像
cv2.imshow("bambi_temp", img)

# 等待按键输入 0 代表任意键
cv2.waitKey(0)

# 保存图像
cv2.imwrite("~/temp.png", img)
