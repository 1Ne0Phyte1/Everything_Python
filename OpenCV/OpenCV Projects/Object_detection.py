from cvzone.ClassificationModule import Classifier
import cv2

cap = cv2.VideoCapture("Res/Spike.mp4")
myClassifier = Classifier()

while True:
    img = cap.read()
    prediction = myClassifier.getPrediction(img)

    cv2.imshow("Image", img)
    cv2.waitKey(2)