import cv2

image = cv2.imread('../Images/1070182.jpg')

print(image.shape)

image_cropped = image[0:500,0:700]

cv2.imshow('image',image)
cv2.imshow('image_cropped',image_cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()