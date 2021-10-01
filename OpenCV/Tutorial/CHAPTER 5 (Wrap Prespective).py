import cv2
import numpy as np

img = cv2.imread("../Res/king.jpg")

width, height = 250,350
pts1 = np.float32([[540,220],[980,232],[285,620],[910,700]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
while True:
    if cv2.waitKey(10) & 0xFF ==ord('q'):
        break