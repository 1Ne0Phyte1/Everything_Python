import cv2
import numpy as np
path = "../Res/S2.jpg"

#Code for stacking images with with different chanels or properties
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


#Defining function for Contours
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>100: #This give only those shape with more than 100 area
            #Drawing contours on Shapes
            cv2.drawContours(imgContours, cnt, -1, (255, 0, 0), 2)
            perimeter = cv2.arcLength(cnt,True)
            print(perimeter)
            #Finding number of sides
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor ==8:
                objectType ="Circle"
            elif objCor ==3:
                objectType = "Tri"
            elif objCor ==4:
                aspRatio = w/float(h)
                if aspRatio>0.95 and aspRatio<1.05:
                    objectType = "Square"   #There is a error here the formula defins square but the ouput shape is rectangle
                else:
                    objectType = "Rectanlge"
                objectType = "Rectangle"
            elif objCor ==5:
                objectType = "Pentagon"
            elif objCor ==6:
                objectType = "Hexagon"
            else:
                objectType = "None"

            cv2.rectangle(imgContours,(x,y),(x+w,y+h),(0.225,0),2)
            cv2.putText(imgContours,objectType,(x+(w//2)-10, y+(h//2)-10),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0,0,0),2)


img = cv2.imread(path)
imgContours = img.copy()




#Converting Img to Gray img
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Creating Blur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

#Canny Img
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
#Blank Img
imgBlank = np.zeros_like(img)

#Stacking imgs
imgStack = stackImages(1,([img,imgGray,imgBlur],
                       [imgCanny,imgContours,imgBlank]))

# cv2.imshow("Original",img)
# cv2.imshow("Gray",imgGray)
# cv2.imshow("Blur",imgBlur)
cv2.imshow("Stack",imgStack)


cv2.waitKey(0)