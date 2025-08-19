from unittest import TestResult
import cv2
import numpy as np
from PIL import Image
import handtrackmodule as ht
import base64
import io
from groq import Groq
import streamlit as st

st.set_page_config(page_title= 'Math with Gestures using AI',layout='wide')
st.title('Math with Gestures using AI')

col1,col2 = st.columns([3,2])

with col1:
    run = st.checkbox('Run',value= True)
    stop = st.checkbox('Stop',value= False)
    FRAME_WINDOW = st.image([])
with col2:
    st.title('Response from AI')
    output_text_area = st.subheader('')

# Initialize camera only when needed
cap = None
canvas = None
prev_pos = None 
detector = ht.handDetector()

def initialize_camera():
    global cap
    if cap is None:
        cap = cv2.VideoCapture(0)
        cap.set(3,1280)
        cap.set(4,720)
    return cap

def release_camera():
    global cap
    if cap is not None:
        cap.release()
        cap = None

def getHandInfo(frame):
    frame = detector.findHands(frame)
    lmlist = detector.findPosition(frame)
    if lmlist:
        fingers = detector.fingersUp(lmlist)
        return fingers,lmlist
    else:
        return None

def draw(info,prev_pos,canvas):
    fingers,lmlist = info
    current_pos = None
    if fingers == [1,1,0,0,0]:
        current_pos = lmlist[8][1:3]
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas,current_pos,prev_pos,(255,0,255),10)
    elif fingers == [0,0,0,0,0]:
        canvas = np.zeros_like(canvas)
    return current_pos,canvas


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def process_image(canvas,fingers):
    if fingers==[1,1,1,1,1]:
        cv2.imwrite("canvas.png",canvas)
        image_path = "canvas.png"
        # Save canvas as canvas.png
        base64_image = encode_image(image_path)

        client = Groq(api_key="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")

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "you are a math teacher and can analyse the image and based on your knowledge you can understand the problem on your own and solve the problem in the image"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            model="meta-llama/llama-4-maverick-17b-128e-instruct",
        )

        return chat_completion.choices[0].message.content
    else:
        return None

response = ""

# Main processing loop
if run and not stop:
    cap = initialize_camera()
    while run and not stop:
        success,img = cap.read()
        img = cv2.flip(img,1)
        if not success:
            break
        info = getHandInfo(img)
        if canvas is None:
            canvas = np.zeros_like(img,np.uint8)
        if info:
            fingers,lmlist = info
            #print(fingers)
            # print(lmlist)
            prev_pos,canvas = draw(info,prev_pos,canvas)
            response = process_image(canvas,fingers)
            if response:
                print('AI Response: ',response)
        frame_combined = cv2.addWeighted(img,0.5,canvas,0.5,0)
        FRAME_WINDOW.image(frame_combined,channels='BGR')
        if response:
            output_text_area.text(response)
        #cv2.imshow('Image',frame_combined)
        #cv2.imshow('Canvas',canvas) 

        if cv2.waitKey(30)==27:
            break
else:
    # Stop camera when stop is checked or run is unchecked
    release_camera()
    if canvas is not None:
        canvas = None
    prev_pos = None
    response = ""
    output_text_area.text("Camera stopped")

# Clean up when the app is closed
if cap is not None:
    cap.release()
cv2.destroyAllWindows()







