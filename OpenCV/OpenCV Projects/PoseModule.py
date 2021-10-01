import cv2
import time
import mediapipe as mp

class poseDetector():

    def __init__(self, mode = False, upperBody = False, smooth = True, detectionCon = 0.5, trackCon = 0.5):

        self.mode = mode
        self.upperBody = upperBody
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpPose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils
        self.pose = self.mpPose.Pose(self.mode, self.upperBody, self.detectionCon, self.trackCon)

    def findPose(self, img, draw =True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        # print(results.pose_landmarks)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                        h, w, c = img.shape
                        #print(id, lm)
                        cx,cy = int(lm.x*w), int(lm.y*h)
                        lmList.append([id,cx,cy])
                        if draw:
                            cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)

        return lmList



def main():
    cap = cv2.VideoCapture("Res/v1.mp4")
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])
        # To draw a circle on perticular spot
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0,0,255), cv2.FILLED)
        # To draw a line betwrrn perticular spots
        cv2.line(img, (lmList[14][1], lmList[14][2]), (lmList[15][1],lmList[15][2]),(0,0,255),3)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 00, 00))
        cv2.imshow("Video", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()