import cv2

image = cv2.imread('../Images/shapes.png')

imagecopy = image.copy()

imageGray = cv2.cvtColor(imagecopy,cv2.COLOR_BGR2GRAY)

imagecanny = cv2.Canny(imageGray,50,50)

contours,hierarchy = cv2.findContours(imagecanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    #print('Area:',area)
    if area>1000:
        cv2.drawContours(imagecopy,cnt,-1,(255,0,255),3)
        peri = cv2.arcLength(cnt,True)
        #print('Perimeter:',peri)
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        #print('length of approx:',len(approx))
        cv2.drawContours(imagecopy,approx,-1,(0,0,255),8)

        x,y,w,h = cv2.boundingRect(approx)
        cv2.rectangle(imagecopy,(x,y),(x+w,y+h),(0,255,0),2)

        if len(approx)==3:
            objType = 'Triangle'
        elif len(approx)>4:
            objType = 'Circle'
        elif len(approx)==4:
            aspRatio = w/h
            if 0.95<aspRatio<1.05:
                objType = 'Square'
            else:
                objType = 'Rectangle'
        else:
            objType = 'None'

        cv2.putText(imagecopy,objType,(x+w//2,y+h//2),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)


cv2.imshow('image',imagecopy)
cv2.waitKey(0)
cv2.destroyAllWindows()