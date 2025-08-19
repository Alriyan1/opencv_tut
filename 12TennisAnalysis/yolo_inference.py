from unittest import result
from ultralytics import YOLO

model = YOLO("yolo11m.pt")
#results = model.predict('input_videos/input_video.mp4',conf=0.2,save=True)

results = model.track(source='input_videos/input_video.mp4',conf=0.2,save=True,persist=True)







