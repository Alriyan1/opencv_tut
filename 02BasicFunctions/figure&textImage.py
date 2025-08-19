import cv2
import numpy as np

#image = np.zeros((512,512))
 
image = np.zeros((512,512,3),np.uint8)
#image[:] = 255,0,0
image[200:300,100:300] = 0,255,0
print(image.shape)

cv2.line(image,(100,300),(500,300),(0,0,255),3)
cv2.rectangle(image,(0,0),(300,250),(0,0,255),3)
cv2.circle(image,(300,300),(50),(0,0,255),3)
cv2.putText(image,'OpenCV',(100,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()