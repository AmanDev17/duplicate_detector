import os
import cv2
import numpy as np
from PIL import Image
import imagehash

# ==========================
# Configuration Settings
# ==========================
IMAGE_FOLDER = "images"      # Folder containing images to compare
HASH_SIZE = 16               # Size of perceptual hash (16x16 = 256 bits)
HAMMING_THRESHOLD = 30       # Similarity threshold for duplicate detection
# ==========================


def preprocess_image(path):
    """
    Load and preprocess an image:
    - Convert to grayscale
    - Normalize brightness (histogram equalization)
    - Resize while preserving aspect ratio
    - Apply slight Gaussian blur to reduce noise
    """
    img = cv2.imread(path)

    if img is None:
        return None

    # Convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Normalize brightness and contrast
    img = cv2.equalizeHist(img)

    # Resize with padding to maintain aspect ratio
    img = resize_with_padding(img, 256)

    # Reduce minor noise
    img = cv2.GaussianBlur(img, (3, 3), 0)

    return Image.fromarray(img)


def resize_with_padding(img, size):
    """
    Resize image while preserving aspect ratio.
    Pads the image with zeros to create a square image.
    """
    h, w = img.shape
    scale = size / max(h, w)

    new_h = int(h * scale)
    new_w = int(w * scale)

    resized = cv2.resize(img, (new_w, new_h))

    padded = np.zeros((size, size), dtype=np.uint8)

    y_offset = (size - new_h) // 2
    x_offset = (size - new_w) // 2

    padded[y_offset:y_offset + new_h, x_offset:x_offset + new_w] = resized

    return padded


def compute_phash_variants(image):
    """
    Compute perceptual hash for multiple rotations
    to improve rotation robustness.
    """
    rotations = [
        image,
        image.rotate(90, expand=True),
        image.rotate(180, expand=True),
        image.rotate(270, expand=True),
    ]

    return [imagehash.phash(img, hash_size=HASH_SIZE) for img in rotations]


def min_hamming_distance(hashes1, hashes2):
    """
    Compute the minimum Hamming distance
    between all hash combinations.
    """
    return min(h1 - h2 for h1 in hashes1 for h2 in hashes2)


def find_duplicates(folder):
    """
    Scan folder, compute hashes, and identify duplicate images
    based on Hamming distance threshold.
    """
    hashes = {}
    duplicates = []

    print("Scanning images...\n")

    # Generate perceptual hashes for each image
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        if not filename.lower().endswith(
            ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
        ):
            continue

        image = preprocess_image(path)
        if image is None:
            continue

        hashes[filename] = compute_phash_variants(image)

    files = list(hashes.keys())

    if len(files) < 2:
        print("Not enough images to compare.")
        return

    print("Pairwise Comparison Results:\n")

    # Compare each pair of images
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            distance = min_hamming_distance(
                hashes[files[i]],
                hashes[files[j]]
            )

            print(f"{files[i]}  <-->  {files[j]}  | Distance: {distance}")

            if distance <= HAMMING_THRESHOLD:
                duplicates.append((files[i], files[j], distance))

    # Final summary
    print("\n==============================")
    print("Duplicate Summary")
    print("==============================")

    if not duplicates:
        print(f"No duplicates found (threshold = {HAMMING_THRESHOLD}).")
    else:
        for file1, file2, distance in duplicates:
            print(
                f"{file1} is considered duplicate of "
                f"{file2} (Distance: {distance})"
            )


if __name__ == "__main__":
    find_duplicates(IMAGE_FOLDER)