import cv2
import numpy as np
import mediapipe as mp
import time
import handtrackmodule as ht

frameWidth = 700
frameHeight = 640

output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (frameWidth, frameHeight))

image_white = cv2.imread('Resources/whiteimage.png')
image_white = cv2.resize(image_white,(frameWidth,frameHeight))

image_wheel = cv2.imread('Resources/spinwheelfinal.png',cv2.IMREAD_UNCHANGED)

image_clip = cv2.imread('Resources/clip_final.png',cv2.IMREAD_UNCHANGED)

cap = cv2.VideoCapture(0)

detector= ht.handDetector()
pitch_threshold = 60
rotationangle = 0 
spinStartTime = 0
angle_adjustments = [
    (3, -50),
    (5, -40),
    (8, -30),
    (10, -25),
    (12, -15),
    (14, -10),
    (16, -5),
    (20, -3)  # Extend the range as needed
]

def overlayPNG(imgBack, imgFront, pos=[0, 0]):

    hf, wf, cf = imgFront.shape
    hb, wb, cb = imgBack.shape

    x1, y1 = max(pos[0], 0), max(pos[1], 0)
    x2, y2 = min(pos[0] + wf, wb), min(pos[1] + hf, hb)

    # For negative positions, change the starting position in the overlay image
    x1_overlay = 0 if pos[0] >= 0 else -pos[0]
    y1_overlay = 0 if pos[1] >= 0 else -pos[1]

    # Calculate the dimensions of the slice to overlay
    wf, hf = x2 - x1, y2 - y1

    # If overlay is completely outside background, return original background
    if wf <= 0 or hf <= 0:
        return imgBack

    # Extract the alpha channel from the foreground and create the inverse mask
    alpha = imgFront[y1_overlay:y1_overlay + hf, x1_overlay:x1_overlay + wf, 3] / 255.0
    inv_alpha = 1.0 - alpha

    # Extract the RGB channels from the foreground
    imgRGB = imgFront[y1_overlay:y1_overlay + hf, x1_overlay:x1_overlay + wf, 0:3]

    # Alpha blend the foreground and background
    for c in range(0, 3):
        imgBack[y1:y2, x1:x2, c] = imgBack[y1:y2, x1:x2, c] * inv_alpha + imgRGB[:, :, c] * alpha

    return imgBack

def rotate_image(img,angle): 
    (h,w) = img.shape[:2]
    center = (w//2,h//2)
    M = cv2.getRotationMatrix2D(center,angle,1.0)
    rotated_img = cv2.warpAffine(img,M,(w,h),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_CONSTANT,borderValue=(255,0,0))
    return rotated_img

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    img = cv2.resize(img,(frameWidth,frameHeight))
    if not success:
        break

    img = detector.findHands(img)
    lmlist = detector.findPosition(img)
    if len(lmlist) != 0:
        thumb=(lmlist[4][1],lmlist[4][2])
        indexfinger = (lmlist[8][1],lmlist[8][2])
        cv2.circle(img,thumb,15,(100,255,100),cv2.FILLED)
        cv2.circle(img,indexfinger,15,(100,255,100),cv2.FILLED)

        pitch_distance = cv2.norm(indexfinger,thumb)
        #print(pitch_distance)
        x,y = 560,240
        distance_index = cv2.norm(indexfinger,(x,y))
        if pitch_distance<pitch_threshold and distance_index<50:
            spinStartTime = 0 
            rotationangle -= 150
            if spinStartTime == 0:
                spinStartTime = time.time()
    if spinStartTime != 0:
        elapsedTime = time.time() - spinStartTime
        for threshold,angle in angle_adjustments:
            if elapsedTime < threshold:
                rotationangle += angle
                break
        
    img = cv2.addWeighted(img,0.2,image_white,0.8,0)
    image_wheel_rot = rotate_image(image_wheel,rotationangle)
    img = overlayPNG(img,image_wheel_rot,(150,100))
    img = overlayPNG(img,image_clip,(480,210))
    output.write(img)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()