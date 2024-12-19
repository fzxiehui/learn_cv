import cv2

import os
# 将工作目录更改为该脚本所在的文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 读取图像
img = cv2.imread("../bambi.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 120,255, cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)

# mode 检索模式
# 
# cv2.RETR_EXTERNAL - > 外轮廓
# cv2.RETR_LIST - > 所有轮廓到列表
# cv2.RETR_CCOMP -> 所有轮廓 -> 两层 外，内
# cv2.RETR_TREE -> 所有轮廓到树形
# 
# method: (逼近方法)
#
# cv2.CHAIN_APPROX_NONE  Freeman 链码方式所有其他方法输出多边形
# cv2.CHAIN_APPROX_SIMPLE 压缩水平、垂直
contours, hierarchy = cv2.findContours(image=thresh, 
        mode=cv2.RETR_CCOMP, 
        method=cv2.CHAIN_APPROX_NONE | cv2.CHAIN_APPROX_SIMPLE)

draw_img = img.copy()
# -1 = 全部
res = cv2.drawContours(draw_img, contours, -1, (0, 0, 255), 5)
# res = cv2.drawContours(draw_img, contours, 0, (0, 0, 255), 5)

cv2.imshow("draw_img", draw_img)
cv2.waitKey(0)

cnt = contours[0]
print(cv2.contourArea(cnt))
print(cv2.arcLength(cnt, True))
