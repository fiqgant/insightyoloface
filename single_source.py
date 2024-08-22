import cv2
import numpy as np
import csv
from insightface.app import FaceAnalysis

# Load YOLO-Face
net = cv2.dnn.readNet("models/yolov3-wider_16000.weights", "models/yolov3-face.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Initialize InsightFace
def initialize_arcface():
    app = FaceAnalysis(allowed_modules=['detection', 'recognition'])
    app.prepare(ctx_id=0, det_size=(640, 640))  # You can adjust the det_size if needed
    return app

# Initialize the models
arcface_app = initialize_arcface()

# Video
cap = cv2.VideoCapture('Video/Lab3/kamera di jam 3.06.mp4')

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # YOLO-Face Detection
    blob = cv2.dnn.blobFromImage(small_frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    faces_yolo = []
    confidences = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            confidence = scores[0]  # YOLO-Face only has one class ('face')
            if confidence > 0.5:
                center_x = int(detection[0] * small_frame.shape[1])
                center_y = int(detection[1] * small_frame.shape[0])
                w = int(detection[2] * small_frame.shape[1])
                h = int(detection[3] * small_frame.shape[0])
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                faces_yolo.append((x, y, w, h))
                confidences.append(float(confidence))

    # Non-Maximum Suppression to reduce overlapping boxes
    indices = cv2.dnn.NMSBoxes(faces_yolo, confidences, 0.5, 0.4)
    
    # If indices is not empty, proceed with filtering faces
    if len(indices) > 0:
        indices = indices.flatten()  # Ensure indices are flattened to a 1D array
        faces_yolo = [faces_yolo[i] for i in indices]
    else:
        faces_yolo = []

    # InsightFace Detection
    faces_arcface = arcface_app.get(frame)
    
    # Draw bounding boxes for YOLO-Face
    for i, (x, y, w, h) in enumerate(faces_yolo):
        # Adjust bounding box to original frame size
        x, y, w, h = x*2, y*2, w*2, h*2
        accuracy_yolo = confidences[i]  # Use YOLO confidence as accuracy
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green box for YOLO
        cv2.putText(frame, f"YOLO Accuracy: {accuracy_yolo:.2f}", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Draw bounding boxes for InsightFace
    for i, face in enumerate(faces_arcface):
        bbox = face.bbox.astype(int)
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 0), 2)  # Blue box for InsightFace
        cv2.putText(frame, f"InsightFace Accuracy: {1.0:.2f}", (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Display the total number of faces detected by each model
    cv2.putText(frame, f'Total YOLO Faces: {len(faces_yolo)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f'Total InsightFace Faces: {len(faces_arcface)}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the frame with bounding boxes and face counts
    cv2.imshow('Face Detection', frame)

    frame_count += 1

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
