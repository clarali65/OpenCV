import cv2 as cv
import numpy as np
img1=cv.imread("C:/Users/ausu/Desktop/sample.jpg")
roi_img=np.zeros(img1.shape[0:2],dtype=np.uint8)
roi_img[100:280,200:300]=255 #mask generation

img_add=cv.add(img1,img1)#相加的两个图片应该有相同的大小和通道
img_add_mask=cv.add(img1,img1,mask=roi_img)
cv.imshow("roi_img",roi_img)
cv.imshow("img_add",img_add)
cv.imshow("img_add_mask",img_add_mask)

cv.waitKey(0)#表示无限等待
#while(char(waiteKey(1))!='q'){}
#输入字符则waitKey()返回当前字符的ASCII码对应的十进制值
#然后char()将ASCII码转换为字符，最后判断是否与‘q’对等
#若键入字符为q，则停止循环，窗口不再等待，即退出窗口
#去掉char也可以
cv.destroyAllWindows()

img2=cv.imread(r"C:/Users/ausu/Desktop/sample2.jpg")
img=img1[0:426,43:683]
blend=cv.addWeighted(img,0.5,img2,0.9,0)
cv.imshow("blend",blend)
cv.waitKey(0)
cv.destroyAllWindows()