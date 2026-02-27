# Duplicate Image Detector (pHash + OpenCV)

## Overview

This project is a robust local duplicate image detection tool built using Python, OpenCV, and Perceptual Hashing (pHash). It detects visually similar images even if they differ in brightness, rotation, scaling, or minor distortions.

The system performs preprocessing, generates perceptual hashes, and compares images using Hamming distance to determine similarity.

---

## Features

- Perceptual Hashing (pHash) for visual similarity detection  
- Hamming Distance–based comparison  
- Brightness normalization using histogram equalization  
- Rotation handling (0°, 90°, 180°, 270°)  
- Aspect ratio–preserving resizing with padding  
- Noise reduction using Gaussian blur  
- Adjustable similarity threshold  
- Local folder-based batch processing  
- Lightweight and efficient execution  

---

## Technology Stack

- Python 3.8+
- OpenCV
- Pillow
- NumPy
- ImageHash

---

## Project Structure
Duplicate_Detector/
│
├── dup_detect.py
├── requirements.txt
├── images/
│ ├── image1.jpg
│ ├── image2.jpg
| ├── image3.jpg
│ └── image4.jpg
│
└── README.md


Place all images to be analyzed inside the `images/` directory.

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Duplicate_Detector
```
## Requirements

This project includes a `requirements.txt` file to simplify dependency management and ensure consistent environments across systems.

### Installation

Install all required dependencies using:

```bash
pip install -r requirements.txt
```
opencv-python>=4.8.0
pillow>=10.0.0
numpy>=1.24.0
ImageHash>=4.3.1

To run this Script
```bash
python dup_detect.py
```
The script will:

Load all supported images from the images/ folder

Preprocess each image (grayscale conversion, normalization, resize, blur)

Generate perceptual hashes for multiple rotations

Compute pairwise Hamming distances

Report duplicate image pairs based on the configured threshold

Configuration

Inside dup_detect.py:

IMAGE_FOLDER = "images"
HASH_SIZE = 16
HAMMING_THRESHOLD = 30
Threshold Guide
Threshold Range	Sensitivity Level
10–15	Very strict
20–30	Balanced (Recommended)
40–50	Very lenient

Lower threshold values increase strictness.
Higher threshold values increase tolerance to brightness and rotation variations.

How It Works

Convert image to grayscale

Normalize brightness using histogram equalization

Resize while preserving aspect ratio with padding

Apply Gaussian blur to reduce noise

Compute perceptual hash (pHash) using Discrete Cosine Transform (DCT)

Compare image hashes using Hamming distance

Evaluate multiple rotation variants for robustness

Lower Hamming distance indicates higher similarity.

Example Output
image1.jpg  <-->  image2.jpg  | Distance: 12
Duplicate: image1.jpg is similar to image2.jpg (Distance: 12)
Supported Image Formats

.jpg

.jpeg

.png

.bmp

.tiff

Use Cases

Dataset cleaning

Photo library deduplication

Document scanning cleanup

AI training data preprocessing

Digital archive management

Future Improvements

Graphical User Interface (GUI)

Recursive folder scanning

Automated duplicate removal option

Hybrid similarity scoring (pHash + SSIM)

Cloud-based processing version

GPU acceleration

License

This project is open-source and intended for educational and research purposes.
