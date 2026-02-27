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

Place all images to be analyzed inside the `images/` directory.

---

## Installation

### 1. Clone the Repository

```bash
git clone <https://github.com/AmanDev17/duplicate_detector/tree/main>
cd duplicate_Detector
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

## Script Workflow

1. Load all supported images from the `images/` folder.  
2. Preprocess each image (grayscale conversion, normalization, resize, blur).  
3. Generate perceptual hashes for multiple rotations (0°, 90°, 180°, 270°).  
4. Compute pairwise Hamming distances between image hashes.  
5. Report duplicate image pairs based on the configured threshold.  

---

## Configuration

Inside `dup_detect.py`:

```python
IMAGE_FOLDER = "images"
HASH_SIZE = 16
HAMMING_THRESHOLD = 30
```

### Threshold Guide

1. **10–15** → Very strict  
2. **20–30** → Balanced (Recommended)  
3. **40–50** → Very lenient  

Lower threshold values increase strictness.  
Higher threshold values increase tolerance to brightness and rotation variations.

---

## How It Works

1. Convert image to grayscale.  
2. Normalize brightness using histogram equalization.  
3. Resize while preserving aspect ratio using padding.  
4. Apply Gaussian blur to reduce noise.  
5. Compute perceptual hash (pHash) using Discrete Cosine Transform (DCT).  
6. Compare image hashes using Hamming distance.  
7. Evaluate multiple rotation variants for robustness.  

Lower Hamming distance indicates higher similarity.

---

## Example Output

```bash
image1.jpg  <-->  image2.jpg  | Distance: 12
Duplicate: image1.jpg is similar to image2.jpg (Distance: 12)
```

---

## Supported Image Formats

1. `.jpg`  
2. `.jpeg`  
3. `.png`  
4. `.bmp`  
5. `.tiff`  

---

## Use Cases

1. Dataset cleaning  
2. Photo library deduplication  
3. Document scanning cleanup  
4. AI training data preprocessing  
5. Digital archive management  

---

## Future Improvements

1. Graphical User Interface (GUI)  
2. Recursive folder scanning  
3. Automated duplicate removal option  
4. Hybrid similarity scoring (pHash + SSIM)  
5. Cloud-based processing version  
6. GPU acceleration  

---

## License

1. This project is open-source.  
2. Intended for educational and research purposes.  
