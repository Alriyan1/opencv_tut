import cv2 
import numpy as np

image = cv2.imread('../Images/documentscanner.jpg')

#print(image.shape)

image = cv2.resize(image,(700,800))
imagecopy = image.copy()

def preprocess(image):

    imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    imageCanny = cv2.Canny(imageGray,200,200)
    
    return imageCanny

def findContours(image):
    contours,hierarchy = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    maxArea = 0
    biggest = np.array([])
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>100:
            cv2.drawContours(imagecopy,cnt,-1,(0,0,255),2)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            #print(len(approx))
            if area>maxArea and len(approx)==4:
                maxArea = area
                biggest = approx
    cv2.drawContours(imagecopy,approx,-1,(0,255,255),8)


    return biggest,imagecopy

def getWrap(image,biggest):
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0,0],[650,0],[0,750],[650,750]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)

    imageOutput = cv2.warpPerspective(image,matrix,(650,750))
    imagecropped = imageOutput[20:imageOutput.shape[0]-20,20:imageOutput.shape[1]-20]
    return imagecropped

def reorder(myPoints):

    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    #print(diff)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew

imageCanny = preprocess(image)
biggest,contours = findContours(imageCanny)
# print(biggest.size)

if biggest.size!=0:
    reordered = reorder(biggest)
    imageWrap = getWrap(image,reordered)
    cv2.imshow('imageWrap',imageWrap) 
    cv2.imshow('image',contours)
else:
    cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()