#coding:utf-8
import cv2
img=cv2.imread(r"C:/Users/ausu/Desktop/sample.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img_threshold=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("img",img)
cv2.imshow("thre",img_threshold)

key=cv2.waitKey(0)
if key==27:#esc的ASCII值为27
    print(key)
    cv2.destroyAllWindows()#实现在delaytime内正常退出
cv2.imwrite(r"C:/Users/ausu/Desktop/thre.jpg",img_threshold)