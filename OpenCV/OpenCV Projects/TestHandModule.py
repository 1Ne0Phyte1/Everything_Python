#This is an example to show how we can im port from HandTrackingModule

import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm




pTime = 0
cTime = 0
cap = cv2.VideoCapture(" ")
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img,draw= False)  #you can write "draw = False" to remove drawing/line on your hand
    lmList = detector.findPosition(img, draw= False) #you can write "draw = False" to remove drawing/line on your hand
    if len(lmList) != 0:
        print(lmList[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

    cv2.imshow("Imgame", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break