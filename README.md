# duplicate_detector
This project detects visually similar images using perceptual hashing (pHash) and Hamming distance. Images are preprocessed with grayscale conversion, brightness normalization, resizing, and blur. Hashes are computed for multiple rotations to improve robustness. If similarity distance ≤ 30, images are flagged as duplicates.
