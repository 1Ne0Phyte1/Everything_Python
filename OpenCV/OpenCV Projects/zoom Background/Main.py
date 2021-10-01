import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(' ')
cap.set(3, 500)
cap.set(4, 500)
cap.set(cv2.CAP_PROP_FPS, 60)

# Removing BG
segmentor = SelfiSegmentation(1)

# fps
fpsReader = cvzone.FPS()

# importing Images
# imgBG = cv2.imread("BG Images/1.jpg")

# listing all images from folder

listImg = os.listdir("BG Images")
print(listImg)
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'BG Images/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 0

while True:
    success, img = cap.read()

    # removes BG
    # For colored background
    # imgOut = .removeBG(img, (255, 0, 255), threshold=0.1)

    # for image background
    # imgOut = segmentor.removeBG(img, imgBG, threshold=0.1)

    # for changeing image background
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.9)

    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    _, imgStacked = fpsReader.update(imgStacked, color=(0, 0, 255))

    print(indexImg)

    cv2.imshow("ImageOut", imgStacked)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(imgList) - 1:
            indexImg += 1
    elif key == ord('q'):
        break
