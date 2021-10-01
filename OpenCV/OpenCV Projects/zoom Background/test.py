import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(' ')
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv2.CAP_PROP_FPS, 60)

# Removing BG
seg = SelfiSegmentation(0)

while True:
    success, img = cap.read()
    imgOut = seg.removeBG(img, (0, 255, 0))

    cv2.imshow("ImageOut", img)
    cv2.waitKey(1)
