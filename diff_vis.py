import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def load_images(image_paths):
    images = []
    for path in image_paths:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise ValueError(f"Image at {path} could not be loaded.")
        images.append(img.astype(np.float32))
    return images

def compute_differences(images):
    diffs = []
    for i in range(len(images) - 1):
        diff = cv2.absdiff(images[i+1], images[i])  # absolute difference
        diffs.append(diff)
    return diffs

def animate_differences(differences):
    fig, ax = plt.subplots()
    im = ax.imshow(differences[0], cmap='gray', vmin=0, vmax=255)
    ax.axis('off')

    def update(frame):
        im.set_array(differences[frame])
        return [im]

    anim = FuncAnimation(fig, update, frames=len(differences), interval=1000, blit=True)
    plt.show()

def main(image_paths, n):
    if len(image_paths) < n:
        raise ValueError("Not enough images provided")
    images = load_images(image_paths[-n:])
    diffs = compute_differences(images)
    animate_differences(diffs)


main([
    "capture_192_168_0_17_0.jpg",
    "capture_192_168_0_17_1.jpg",
    "capture_192_168_0_17_2.jpg",
    "capture_192_168_0_17_3.jpg",
    "capture_192_168_0_17_4.jpg",
    "capture_192_168_0_17_5.jpg",
    "capture_192_168_0_17_6.jpg",
    "capture_192_168_0_17_7.jpg",
    "capture_192_168_0_17_8.jpg",
    "capture_192_168_0_17_9.jpg",
    # "capture_192_168_0_64_0.jpg",
    # "capture_192_168_0_64_1.jpg",
    # "capture_192_168_0_64_2.jpg",
    # "capture_192_168_0_64_3.jpg",
    # "capture_192_168_0_64_4.jpg",
    # "capture_192_168_0_64_5.jpg",
    # "capture_192_168_0_64_6.jpg",
    # "capture_192_168_0_64_7.jpg",
    # "capture_192_168_0_64_8.jpg",
    # "capture_192_168_0_64_9.jpg",
], 3)
