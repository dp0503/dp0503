from PIL import Image, ImageEnhance
import os

img = Image.open("source-photo.png")
w, h = img.size

# The image is 4000x2250. The face is mostly on the left-center.
# We'll take a square of size `h` (2250).
# Let's start the crop from x=w*0.1 (so x=400) to keep the face centered.
size = h
start_x = int(w * 0.1)

crop_box = (start_x, 0, start_x + size, size)
img_cropped = img.crop(crop_box)

# Convert to grayscale
img_gray = img_cropped.convert("L")

# Increase contrast a bit
enhancer = ImageEnhance.Contrast(img_gray)
img_contrast = enhancer.enhance(1.5)

# Save as source-prepped.png
img_contrast.save("source-prepped.png")
print("Saved source-prepped.png using simple PIL crop")
