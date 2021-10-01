import cv2
import time
import os
from Tutorial import HandTrackingModule as htm

########################################
wCam = 640
hCam = 480
pTime = 0
########################################
cap = cv2.VideoCapture(" ")
cap.set(3, wCam)
cap.set(4, hCam)

#importing Images
folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imgPath in myList:
    image = cv2.imread(f'{folderPath}/{imgPath}')
    # print(f'{folderPath}/{imgPath}')
    overlayList.append(image)

print(len(overlayList))

#Hand Tracking
detector = htm.handDetector(detectionCon= 0.75)

#Tips of the Fingers
tipIds = [4, 8, 12, 16, 20]

while True:
   success, img = cap.read()
   img = detector.findHands(img)
   lmList = detector.findPosition(img, draw=False)
   #print(lmList)

   if len(lmList) != 0 :
       fingers = []

       #This is for the thumb
       if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:  # Here [8] represents the point on the finger and [2] represents y axis and [1] represents  axis
           fingers.append(1)
       else:
           fingers.append(0)

       #This loop is for four fingers, cause thub doesn't follow the same rule
       for id in range(1,5):
           if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:  #Here [8] represents the point on the finger and [2] represents y axis and [1] represents  axis
               fingers.append(1)
           else:
               fingers.append(0)
               #print("Index Finger open")

       #print(fingers)
       totalFingers = fingers.count (1)
       print(totalFingers)

       #Fitting IMg on to the output window
       h ,w, c = overlayList[totalFingers].shape
       img[0:h, 0:w] = overlayList[totalFingers]

       cv2.rectangle(img, (0,400), (150, 580), (0, 255, 0), cv2.FILLED)
       cv2.putText(img, str(totalFingers), (0, 550), cv2.FONT_HERSHEY_COMPLEX_SMALL, 10, (255, 0, 2), 25)

   #FPS
   cTime = time.time()
   fps = 1/(cTime-pTime)
   pTime = cTime

   cv2.putText(img,f'FPS:{int(fps)}',(400,70), cv2.FONT_HERSHEY_PLAIN,3, (255,0,0),3)
   cv2.imshow("IMG", img)
   if cv2.waitKey(1) & 0xFF ==ord('q'):
       break



