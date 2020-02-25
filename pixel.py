#像素值获取
import cv2
import matplotlib.pyplot as plt
img=cv2.imread(r"C:/Users/ausu/Desktop/sample.jpg")
pixel=img[100][100]
img[100][100]=[59,94,99]
b=img[100][100][0]#blue
g=img[100][100][1]#green
r=img[100,100,2]#red
r=img[100,100,2]=99
pixel=img.item(100,100,2)
img.itemset((100,100,2),99)

#图片性质

#row,cols,channels
img.shape
#size
img.size
#type
img.dtype

#ROI,range of interest
roi=img[100:200,300:400]#row:100~200,col:300~400
img[50:150,200:300]=roi
b=img[:,:,0]
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

#padding
img2=cv2.imread(r"C:/Users/ausu/Desktop/sample.jpg")
img=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
constant=cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_CONSTANT,value=[0,255,0])
reflect=cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REFLECT)
reflect101=cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REFLECT101)
replicate=cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REPLICATE)
wrap=cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_WRAP)
titles=["constant","reflect","reflect101","replicate","wrap"]
images=[constant,reflect,reflect101,replicate,wrap]
for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()