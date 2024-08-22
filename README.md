# InsightYOLOFace

*Read in [Bahasa Indonesia](README_ID.md)*

This repository contains scripts for face detection using YOLOv3 and face recognition using InsightFace. It also includes a combined script that leverages both YOLOv3 and InsightFace for face detection.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [YOLOv3 Face Detection](#yolov3-face-detection)
  - [InsightFace Face Recognition](#insightface-face-recognition)
  - [Combined YOLOv3 and InsightFace](#combined-yolov3-and-insightface)
  - [Specifying the Video Source](#specifying-the-video-source)
- [Platform-Specific Instructions](#platform-specific-instructions)
  - [Windows](#windows)
  - [macOS (Apple)](#macos-apple)
  - [Linux](#linux)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository provides the following Python scripts:

- **`yolov3.py`**: Detects faces in a video using the YOLOv3 model.
- **`insightface.py`**: Performs face detection using the InsightFace model.
- **`combined.py`**: Combines YOLOv3 and InsightFace to detect faces using YOLOv3 and InsightFace.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- InsightFace

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/fiqgant/arcyoloface.git
    cd arcyoloface
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ### Windows:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    ### macOS (Apple) and Linux:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

    If `requirements.txt` is not provided, you can install the packages manually:

    ```bash
    pip install opencv-python numpy insightface
    ```

4. **Download the YOLOv3 model weights:**

    - Place the YOLOv3 weights (`yolov3-wider_16000.weights`) and configuration file (`yolov3-face.cfg`) in the `models` directory. You can download them from [here](https://github.com/sthanhng/yoloface).

## Usage

### YOLOv3 Face Detection

The `yolov3.py` script detects faces in a video using the YOLOv3 model.

1. **Run the YOLOv3 face detection script:**

    ```bash
    python yolov3.py
    ```

2. **Output:**

    The script will display a video with detected faces marked by green bounding boxes, along with the confidence score (accuracy) for each face.

### InsightFace Face Recognition

The `insightface.py` script performs face detection and recognition using the InsightFace model.

1. **Run the InsightFace face recognition script:**

    ```bash
    python insightface.py
    ```

2. **Output:**

    The script will display a video with detected faces marked by blue bounding boxes. For each detected face, it will show an accuracy score.

### Combined YOLOv3 and InsightFace

The `combined.py` script combines YOLOv3 and InsightFace to detect faces using YOLOv3 and recognize them using InsightFace.

1. **Run the combined YOLOv3 and InsightFace script:**

    ```bash
    python combined.py
    ```

2. **Output:**

    The script will display a video with faces detected by YOLOv3 and InsightFace. YOLOv3 detections are marked with green bounding boxes, while InsightFace detections are marked with blue bounding boxes. The accuracy of each detection and the total number of faces detected by each model will be displayed.

### Specifying the Video Source

You can specify the video source in your scripts by editing the `cap = cv2.VideoCapture()` line. Below are examples of how to use different video sources:

#### 1. **Using a Video File (e.g., `video.mov`)**:

```python
cap = cv2.VideoCapture('video.mov')
```

Place the video file in the same directory as your script or provide the full path.

#### 2. **Using a Webcam**:

```python
cap = cv2.VideoCapture(0)
```

This will use the default webcam on your system. If you have multiple webcams, you can change the index (`0`, `1`, etc.) to select a different one.

#### 3. **Using a CCTV Stream (IP Camera)**:

```python
cap = cv2.VideoCapture('rtsp://username:password@ip_address:port/stream')
```

Replace `username`, `password`, `ip_address`, `port`, and `stream` with the appropriate values for your CCTV camera.

- **Example**: If your camera's IP is `192.168.1.100`, port is `554`, and the stream path is `h264`, it would look like this:

  ```python
  cap = cv2.VideoCapture('rtsp://admin:12345@192.168.1.100:554/h264')
  ```

#### 4. **Handling Video Source Failures**:

If the video source fails to open (e.g., file not found or camera not connected), the script will print an error message and exit gracefully:

```python
if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()
```

## Platform-Specific Instructions

### Windows

1. **Install Python 3.x**: Download and install Python from [python.org](https://www.python.org/downloads/windows/).

2. **Install Git**: Download and install Git from [git-scm.com](https://git-scm.com/download/win).

3. **Install OpenCV and Other Dependencies**: Install the required Python packages by following the instructions above.

4. **Run the Scripts**: Use the `cmd` or PowerShell to navigate to your project directory and run the scripts as described in the usage section.

### macOS (Apple)

1. **Install Python 3.x**: Install Python using Homebrew:

    ```bash
    brew install python
    ```

2. **Install Git**: Git is usually pre-installed on macOS. If not, install it using Homebrew:

    ```bash
    brew install git
    ```

3. **Install OpenCV and Other Dependencies**: Follow the installation steps provided above.

4. **Run the Scripts**: Open Terminal, navigate to your project directory, and run the scripts as described in the usage section.

### Linux

1. **Install Python 3.x**: Python is often pre-installed. If not, install it using your package manager (e.g., `apt` for Ubuntu/Debian):

    ```bash
    sudo apt-get install python3 python3-pip
    ```

2. **Install Git**: Install Git using your package manager:

    ```bash
    sudo apt-get install git
    ```

3. **Install OpenCV and Other Dependencies**: Follow the installation steps provided above.

4. **Run the Scripts**: Use Terminal to navigate to your project directory and run the scripts as described in the usage section.

## Results

You can expect the following results from the scripts:

- **YOLOv3**: Green bounding boxes around detected faces with confidence scores.
- **InsightFace**: Blue bounding boxes around recognized faces with accuracy scores.
- **Combined**: Both green and blue bounding boxes, indicating YOLOv3 and InsightFace detections, respectively.

## Contributing

If you have any improvements, bug fixes, or additional features you'd like to see, feel free to fork the repository and create a pull request. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
