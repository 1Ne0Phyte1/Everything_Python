import cv2
import numpy as np

img = cv2.imread("../Res/q.jpg")
kernel = np.ones((5,5),np.uint8)

#Color to Gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Img BLur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

#To fing edges in IMG
imgCanny = cv2.Canny(img,150,200)

#Dialtion, to connect the broken line in Canny IMG
imgDialation = cv2.dilate(imgCanny,kernel, iterations =1)

#IMG Erosion
imgErode = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray IMG",imgGray)
cv2.imshow("Blur IMG",imgBlur)
cv2.imshow("Canny IMG",imgCanny)
cv2.imshow("Dialation IMG",imgDialation)
cv2.imshow("Erosion IMG",imgErode)
while True:
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break