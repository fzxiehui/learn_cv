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

contours, hierarchy = cv2.findContours(image=thresh, 
        mode=cv2.RETR_EXTERNAL, 
        method=cv2.CHAIN_APPROX_NONE)

cnt = contours[0]
epsilon = 5 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)

res = cv2.drawContours(img, [approx], -1, (0, 0, 255), 2)
cv2.imshow("img", img)
cv2.waitKey(0)

cv2.imshow("img", img)
cv2.waitKey(0)
