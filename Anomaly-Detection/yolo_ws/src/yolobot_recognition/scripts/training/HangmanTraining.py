import ultralytics
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # load a pretrained YOLOv8n detection model

model.train(data='/home/samuel/Downloads/Worker_Data/Worker_Data.yaml', epochs=100, patience=30, batch=32, imgsz=640)