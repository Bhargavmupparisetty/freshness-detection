# freshness-detection app

This project demonstrates real-time freshness detection of fruits using the YOLO (You Only Look Once) model with your webcam feed. The model is loaded from a custom-trained `.pt` file, and predictions are shown live on the video stream. This app uses **OpenCV** for video capture and **Ultralytics YOLO** for detecting the freshness of the fruits in real-time.

## Features
- Real-time object detection via webcam.
- Live object annotations on detected objects.
- Uses custom-trained YOLO model (trained with PyTorch).
- Can detect multiple objects in real-time with bounding boxes.

## Prerequisites

Before running the app, you need to install the following dependencies:

- Python 3.8 or higher
- OpenCV (`opencv-python`)
- PyTorch
- YOLO (Ultralytics YOLO)

### Install Dependencies

To install the required libraries, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Bhargavmupparisetty/freshness-detection.git
   cd freshness-detection
