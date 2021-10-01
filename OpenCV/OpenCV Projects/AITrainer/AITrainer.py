import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("Res/test.webm")

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0

while True:
    success , img = cap.read()
    img = cv2.resize(img, (500,500))
    # img = cv2.imread("Res/test.jpg")
    img = detector.findPose(img,False)
    lmList = detector.findPosition(img, False)
    #print(lmList)
    if len(lmList) !=0:
        #Right Arm
        #angle = detector.findAngle(img, 12, 14, 16)
        # Left Arm
        angle = detector.findAngle(img, 11, 13, 15)

        per = np.interp(angle,(202,270), (0,100))
        #print(angle,per)

        Bar = np.interp(angle, [202, 270], [400, 100])

        #Check for the dumbbell curls
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)

        #Bar
        cv2.rectangle(img, (30, 100), (85, 400), (255,0,0), 3)
        cv2.rectangle(img, (30, int(Bar)), (85, 400), (155,255,190), cv2.FILLED)
        if Bar > 300:
            cv2.rectangle(img, (30, int(Bar)), (85, 400), (0, 255, 0), cv2.FILLED)
        elif Bar < 200:
            cv2.rectangle(img, (30, int(Bar)), (85, 400), (0, 0, 255), cv2.FILLED)

        cv2.putText(img, f'{int(per)}%', (30, 80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (155, 255, 189), 2)
        if per >89:
            cv2.putText(img, f'{int(per)}%', (30, 80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        elif per < 23:
            cv2.putText(img, f'{int(per)}%', (30, 80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 2)

        #Draw Curl count
        #cv2.rectangle(img, (30,150), (85,400),(0,255,0), cv2.FILLED)
        cv2.putText(img, str(count), (40,450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0,255,255), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (400,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2 ,(255,0,0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

