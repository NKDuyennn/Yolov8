from ultralytics import YOLO
import cv2

model = YOLO("yolov8m.pt")
results = model.predict(show=True, source="0", save=True)

print(results)
