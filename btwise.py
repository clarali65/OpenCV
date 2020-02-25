import cv2 as cv
logo=cv.imread("C:/Users/ausu/Desktop/logo.jpg")
rows,cols=logo.shape[0:2]
img=cv.imread("C:/Users/ausu/Desktop/sample.jpg")
roi=img[0:rows,0:cols]
logo_gray=cv.cvtColor(logo,cv.COLOR_BGR2GRAY)
ret,logo_thres=cv.threshold(logo_gray,200,255,cv.THRESH_BINARY_INV)
logo_fg=cv.add(logo,logo,mask=logo_thres)
logo_thres_inv=cv.bitwise_not(logo_thres)
roi_bg=cv.add(roi,roi,mask=logo_thres_inv)
logo_add=cv.add(logo_fg,roi_bg)
img[0:rows,0:cols]=logo_add

cv.imshow("gray",logo_gray)
cv.imshow("thres",logo_thres)
cv.imshow("fg",logo_fg)
cv.imshow("tinv",logo_thres_inv)
cv.imshow("roi_bg",roi_bg)
cv.imshow("logo_add",logo_add)
cv.imshow("img",img)
cv.waitKey()
cv.destroyAllWindows()


import cv2 as cv
import numpy as np
def nothing(args):
    pass
img=cv.imread(r"C:/Users/ausu/Desktop/logo.jpg")
img_hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.namedWindow('tracks')
cv.createTrackbar("LH","tracks",0,255,nothing)
cv.createTrackbar("LS","tracks",0,255,nothing)
cv.createTrackbar("LV","tracks",0,255,nothing)

cv.createTrackbar("UH","tracks",0,255,nothing)
cv.createTrackbar("US","tracks",0,255,nothing)
cv.createTrackbar("UV","tracks",0,255,nothing)

switch="0:OFF \n1:ON"
cv.createTrackbar(switch,"tracks",0,1,nothing)

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
    cv.waitKey(0)
    cv.destroyAllWindows()