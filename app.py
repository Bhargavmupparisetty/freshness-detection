import requests
from ultralytics import YOLO
import os
import cv2


model_path = "./model/best.pt"

model = YOLO(model_path)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image")
        break

    results = model.predict(frame, imgsz=640)
    annotated_frame = results[0].plot()
    cv2.imshow('YOLO Predictions', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
