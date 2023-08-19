from ultralytics import YOLO

model = YOLO("best.pt")

results = model.predict(source="tested.mp4", show=True)
print(results)

