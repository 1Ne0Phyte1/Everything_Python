import cv2
import mediapipe as mp
import time



cap = cv2.VideoCapture(" ")


#Hand Detection Module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# For increasing Frame Rate
pTime = 0
cTime = 0

while True:
    sucess, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            #Finding the locaiton of dots on the hand and drawing or spicifing a perticular Spot
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*w)
                print(id, cx, cy)
                if id == 4:
                    cv2.circle(img, (cx,cy), 5, (255,0,255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)

    #FPS
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX,3, (255,0,255),3)



    cv2.imshow("Imgame",img)
    if cv2.waitKey(1) &0xFF ==ord('q'):
        break