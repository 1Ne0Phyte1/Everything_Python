import cv2
print("package Imported")


#Import IMG
# img = cv2.imread("Res/e.png")
# cv2.imshow("Output",img)
# cv2.waitKey(0)


# #Import Video
#
# cap = cv2.VideoCapture("Res/result.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break


#Import WebCam

cap = cv2.VideoCapture(" ")
cap.set(3,200)
cap.set(4,500)
cap.set(10,1000)
while True:
    success, img = cap.read()
    cv2.imshow("WebCam",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
