import cv2
import time
import PoseModule as pm


cap = cv2.VideoCapture("Res/v1.mp4")
pTime = 0
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList)
    # # To draw a circle on perticular spot
    # cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0,0,255), cv2.FILLED)
    # # To draw a line between perticular spots
    # cv2.line(img, (lmList[14][1], lmList[14][2]), (lmList[15][1],lmList[15][2]),(0,0,255),3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 00, 00),3)
    cv2.imshow("Video", img)
    cv2.waitKey(50)