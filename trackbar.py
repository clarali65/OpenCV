
import cv2 as cv
import numpy as np
def nothing(args):
    pass
img=cv.imread(r"C:/Users/ausu/Desktop/cap.png")
img_hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.namedWindow('tracks')
cv.createTrackbar("LH","tracks",0,255,nothing)
cv.createTrackbar("LS","tracks",0,255,nothing)
cv.createTrackbar("LV","tracks",0,255,nothing)

cv.createTrackbar("UH","tracks",0,255,nothing)
cv.createTrackbar("US","tracks",0,255,nothing)
cv.createTrackbar("UV","tracks",0,255,nothing)
# 不需要循环但是可以滑动滚动条的滑块
# 靠createTrackbar事件处理
# 可以理解为该函数其实一直运行在后台检测是否有滑块移动这种中断产生
# 当你移动滑块时就会触发中断
# 这时回调函数相当于中断服务函数来处理中断

while(1):
    l_h = cv.getTrackbarPos("LH","tracks")
    l_s = cv.getTrackbarPos("LS", "tracks")
    l_v = cv.getTrackbarPos("LV", "tracks")
    u_h = cv.getTrackbarPos("UH", "tracks")
    u_s = cv.getTrackbarPos("US", "tracks")
    u_v = cv.getTrackbarPos("UV", "tracks")

    lower_b=np.array([l_h,l_s,l_v])
    upper_b=np.array([u_h,u_s,u_v])

    mask=cv.inRange(img_hsv,lower_b,upper_b)#对图像进行分割
    res=cv.add(img,img,mask=mask)

    cv.imshow("img",img)
    cv.imshow("mask",mask)
    cv.imshow("res",res)
    if cv.waitKey(1)==27:
        break