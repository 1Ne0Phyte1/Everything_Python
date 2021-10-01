import cv2
import time
import numpy as np
import math
import HandTrackingModule as htm
#pycaw used to controll Volume on windows
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#############################
wCam, hCam = 500, 500
#############################


cap = cv2.VideoCapture(" ")
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0
circleRadius = 10
circleColor = (255,0,255)
circleColorMin = (0,255,0)
circleColorMax = (0,0,255)
lineColor = (255,0,255)
rectanlgeColor = (255,0,0)
textColor = (125,125,125)


#Hand Detection
detector = htm.handDetector(detectionCon= 0.7)

#pycaw Volume modlue initialization
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
#volume.SetMasterVolumeLevel(0,None)
minVol = volRange[0]
maxVol = volRange[1]
volBar = 0
vol = 0
volPer = 0

while True:
    success, img = cap.read()

    #Hand Detection OutPut
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) !=0:
        #print(lmList[4], lmList[8])    #For Knowing the LandMark of the point on the finger please visit MediPipe website

        #Creating Circle on the point we need
        x1, y1 = lmList[4][1], lmList[4][2] #Here [4] represents id of the point on the finger, [1] and [2] represents x and y values respectively
        x2, y2 = lmList[8][1], lmList[8][2]
        #Finding the center of the line
        cx, cy = (x1+x2)//2, (y1+y2)//2

        #Creating Circles on the point
        cv2.circle(img, (x1,y1),circleRadius, circleColor, cv2.FILLED)
        cv2.circle(img, (x2, y2), circleRadius, circleColor, cv2.FILLED)
        cv2.circle(img, (cx, cy), circleRadius, circleColor, cv2.FILLED)
        #Creating Line Between the point
        cv2.line(img, (x1,y1), (x2,y2), lineColor, 3)

        # Finding Length of the line between the points
        length = math.hypot(x2 - x1, y2 - y1)
        #print(length)

        #Hand Range 30 to 150
        #Volume Range -63.5 to 0

        vol = np.interp(length,[30,150],[minVol,maxVol])
        volBar = np.interp(length, [30, 150], [400, 150])
        volPer = np.interp(length, [30, 150], [0, 100])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length<50:
            cv2.circle(img, (cx,cy), circleRadius, circleColorMin, cv2.FILLED)
        elif length>140:
            cv2.circle(img, (cx, cy), circleRadius, circleColorMax, cv2.FILLED)

    #Creating Volume Percentage bar
    cv2.rectangle(img, (30,150), (85,400),rectanlgeColor, 3)
    cv2.rectangle(img, (30, int(volBar)), (85, 400), rectanlgeColor, cv2.FILLED)
    cv2.putText(img, f'{int(volPer)}%', (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, textColor, 3)

    # Finding FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, textColor, 3)

    cv2.imshow("image",img)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break