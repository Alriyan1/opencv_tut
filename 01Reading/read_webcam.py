import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if success:
        cv2.imshow('webcam',img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()