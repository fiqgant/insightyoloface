import os
import cv2
import numpy as np
import csv

# Load YOLO-Face
net = cv2.dnn.readNet("models/yolov3-wider_16000.weights", "models/yolov3-face.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

def process_video(video_path, output_csv):
    # Video
    cap = cv2.VideoCapture(video_path)

    # Open CSV file to save results
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['Frame', 'Total Faces', 'Average Accuracy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Resize frame for faster detection
            small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

            # Detect faces using YOLO-Face
            blob = cv2.dnn.blobFromImage(small_frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)

            faces_yolo = []
            confidences = []
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    confidence = scores[0]  # YOLO-Face only has one class, which is 'face'
                    if confidence > 0.5:
                        center_x = int(detection[0] * small_frame.shape[1])
                        center_y = int(detection[1] * small_frame.shape[0])
                        w = int(detection[2] * small_frame.shape[1])
                        h = int(detection[3] * small_frame.shape[0])
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
                        faces_yolo.append((x, y, w, h))
                        confidences.append(float(confidence))

            # Use Non-Maximum Suppression to reduce overlapping boxes
            indices = cv2.dnn.NMSBoxes(faces_yolo, confidences, 0.5, 0.4)
            if len(indices) > 0:
                indices = indices.flatten()  # Flatten indices array if it's not empty
                faces_yolo = [faces_yolo[i] for i in indices]

            # Count the total number of faces detected
            total_faces = len(faces_yolo)
            average_accuracy = np.mean(confidences) if confidences else 0.0

            # Save the frame's data to the CSV file
            writer.writerow({'Frame': frame_count, 'Total Faces': total_faces, 'Average Accuracy': average_accuracy})

            frame_count += 1

    # Release video capture
    cap.release()

# Function to process all videos in a given folder
def process_all_videos_in_folder(video_root_folder):
    for root, dirs, files in os.walk(video_root_folder):
        for file in files:
            if file.endswith(('.mp4', '.mov', '.avi', '.mkv')):  # Add more extensions if needed
                video_path = os.path.join(root, file)
                output_csv_path = os.path.join(root, file.rsplit('.', 1)[0] + '_output.csv')
                print(f"Processing video: {video_path}")
                process_video(video_path, output_csv_path)
                print(f"Output saved to: {output_csv_path}")

def main():
    video_root_folder = 'Video'  # Root folder containing all video files and subfolders
    process_all_videos_in_folder(video_root_folder)

if __name__ == '__main__':
    main()
