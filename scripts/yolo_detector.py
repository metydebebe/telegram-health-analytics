from ultralytics import YOLO
from pathlib import Path
import json
import os

model = YOLO("yolov8n.pt")
IMG_DIR = "data/raw/images"
OUTPUT = "data/yolo_results.json"

results = []

for img_path in Path(IMG_DIR).rglob("*.jpg"):
    yolo_out = model(img_path)
    for det in yolo_out[0].boxes.data.tolist():
        x1, y1, x2, y2, conf, cls = det
        results.append({
            "image": str(img_path),
            "class": int(cls),
            "confidence": float(conf)
        })

with open(OUTPUT, "w") as f:
    json.dump(results, f)
