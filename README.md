🖼️ Duplicate Image Detector (pHash + OpenCV)

A robust local duplicate image detection tool built using Python, OpenCV, and Perceptual Hashing (pHash).
It detects visually similar images even if they differ in brightness, rotation, scaling, or minor distortions.

🚀 Features

✅ Perceptual Hashing (pHash)

✅ Hamming Distance similarity comparison

✅ Brightness normalization

✅ Rotation handling (0°, 90°, 180°, 270°)

✅ Resizing & blur preprocessing

✅ Adjustable similarity threshold

✅ Local folder-based detection

✅ Lightweight & fast

🛠 Tech Stack

Python 3.8+

OpenCV

Pillow (optional for extended image support)

NumPy

📂 Project Structure
Duplicate_Detector/
│
├── dup_detect.py
├── images/
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── img3.png
│
└── README.md

Place all images you want to compare inside the images/ folder.

⚙️ Installation

Install dependencies:

pip install opencv-python pillow numpy
▶️ Usage

Run the script:

python dup_detect.py

The script:

Loads all images from the images folder

Preprocesses them (grayscale, normalize, resize, blur)

Generates perceptual hashes

Computes Hamming distance between each pair

Flags duplicates based on threshold

🔧 Configuration

Inside dup_detect.py:

IMAGE_FOLDER = "images"
HASH_SIZE = 16
HAMMING_THRESHOLD = 30
Threshold Guide
Threshold	Sensitivity
10–15	Very strict
20–30	Balanced (Recommended)
40–50	Very lenient

Increase threshold to detect brightness/rotation variants.

🧠 How It Works

Converts image to grayscale

Normalizes brightness

Resizes to fixed dimensions

Applies blur

Computes pHash via DCT

Compares hashes using Hamming distance

Checks multiple rotations for robustness

Lower Hamming distance = more similar images.

📌 Example Output
img1.jpg <-> img2.jpg | Distance: 12 | DUPLICATE
img1.jpg <-> img3.jpg | Distance: 45 | Different
🎯 Use Cases

Dataset cleaning

Photo library deduplication

Document scanning cleanup

AI training data filtering

Archive management

📈 Future Improvements

GUI interface

Recursive folder scanning

Batch deletion option

SSIM hybrid scoring

Cloud version

GPU acceleration

📄 License

Open-source for educational and research use.
