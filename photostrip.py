import cv2
import numpy as np

def combine_images(image_paths, output_path):
    """Stack a list of images vertically and write the result to output_path."""
    images = [cv2.imread(p) for p in image_paths]
 
    missing = [p for p, img in zip(image_paths, images) if img is None]
    if missing:
        raise FileNotFoundError(f"Could not read image(s): {missing}")
 
    strip = np.vstack(images)
    cv2.imwrite(output_path, strip)
    return output_path
 