import os
import cv2
import csv
import time
import numpy as np
from insightface.app import FaceAnalysis

# Inisialisasi model deteksi wajah
def initialize_model():
    app = FaceAnalysis(allowed_modules=['detection'])
    app.prepare(ctx_id=-1, det_size=(640, 640))  # Menggunakan perangkat keras terbaik yang tersedia (M2 Neural Engine)
    return app

# Proses video untuk mendeteksi wajah dan menyimpan hasilnya ke dalam file CSV
def process_video(app, video_path, output_csv):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}.")
        return

    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['Frame', 'Total Faces', 'Average Confidence', 'Processing Time (ms)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            start_time = time.time()

            # Deteksi wajah dalam frame
            faces = app.get(frame)
            total_faces = len(faces)
            confidences = []

            for face in faces:
                bbox = face.bbox.astype(int)
                confidence = face.det_score  # Menggunakan confidence score yang diberikan oleh model
                confidences.append(confidence)
                cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
                cv2.putText(frame, f"Confidence: {confidence:.2f}", (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # Hitung rata-rata confidence dan waktu pemrosesan
            average_confidence = np.mean(confidences) if confidences else 0.0
            processing_time = (time.time() - start_time) * 1000  # Waktu dalam milidetik

            # Simpan data ke file CSV
            writer.writerow({
                'Frame': frame_count,
                'Total Faces': total_faces,
                'Average Confidence': average_confidence,
                'Processing Time (ms)': processing_time
            })

            frame_count += 1

            # Keluar jika 'q' ditekan
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()

# Proses semua video dalam folder
def process_all_videos_in_folder(app, video_root_folder):
    for root, dirs, files in os.walk(video_root_folder):
        for file in files:
            if file.endswith(('.mp4', '.mov', '.avi', '.mkv')):  # Sesuaikan dengan format video yang diinginkan
                video_path = os.path.join(root, file)
                output_csv_path = os.path.join(root, file.rsplit('.', 1)[0] + 'insight_output.csv')
                print(f"Processing video: {video_path}")
                process_video(app, video_path, output_csv_path)
                print(f"Output saved to: {output_csv_path}")

def main():
    app = initialize_model()
    video_root_folder = 'Video'  # Ganti dengan path yang sesuai jika berbeda
    process_all_videos_in_folder(app, video_root_folder)

if __name__ == '__main__':
    main()
