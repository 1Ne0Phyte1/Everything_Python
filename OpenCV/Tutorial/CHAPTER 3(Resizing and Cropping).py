import cv2
import numpy as np

img = cv2.imread('../Res/q.jpg')
print("Normal",img.shape)


#Resiging IMG
imgResize = cv2.resize(img,(300,200)) #300 is width, 200 is height
print("Resized",imgResize.shape)


#Cropping IMG
imgCrop = img[0:200,100:270] #0:200 is height, 200:500 is width

cv2.imshow("Image", img)
cv2.imshow("ImageResize", imgResize)
cv2.imshow("ImageCropped", imgCrop)

while True:
    if cv2.waitKey(0) &0xFF ==ord('q'):
        break