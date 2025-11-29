# Image Smoothing using Convolution
from PIL import Image, ImageFilter, ImageOps
import matplotlib.pyplot as plt
import os
# Ensure assets/ folder exists
os.makedirs("assets", exist_ok=True)

# 1. Load Image
img = Image.open("./assets/realPhoto.jpg")

# 2. Resize image to 500x500 pixels
img_resized = img.resize((500, 500))

# 3. Convert image to grayscale
img_gray = ImageOps.grayscale(img_resized)

# 4. Apply Gaussian Smoothing
img_gaussian = img_gray.filter(ImageFilter.GaussianBlur(radius=3))

# 5. Apply Box (Mean) Filter
img_box = img_gray.filter(ImageFilter.BoxBlur(radius=3))

# 6. Save all output images into assets/
img_resized.save("assets/resized_500x500.jpg")
img_gray.save("assets/grayscale.jpg")
img_gaussian.save("assets/gaussian_filtered.jpg")
img_box.save("assets/box_filtered.jpg")

# 7. Display Results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img_resized)
plt.title("Resized 500x500")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(img_gray, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(img_gaussian, cmap="gray")
plt.title("Gaussian Filtered")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(img_box, cmap="gray")
plt.title("Box Filtered")
plt.axis("off")

plt.tight_layout()
plt.show()
