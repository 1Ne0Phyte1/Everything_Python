import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape)
print(img)

# img[:] = 255,0,0

# Creating Images/Shapes
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (255, 0, 152), 2, cv2.FILLED)
cv2.circle(img, (100, 100), 250, (0, 0, 255), 4, cv2.FILLED)

#Typing Text
cv2.putText(img,"OpenCV",(300,300),cv2.FONT_HERSHEY_SIMPLEX,1,(250,150,0),2)
cv2.imshow("Image", img)

while True:
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
