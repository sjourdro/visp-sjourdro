import sys
import numpy as np
import matplotlib.pyplot as plt

# ViSP Python bindings
from visp.core import ImageGray, ImageRGBa, Color


# Create ViSP images
I_gray = ImageGray(800, 800, 125)		# grayscale image
I_rgba = ImageRGBa(800, 800, Color.red)	# RGBa image


# Convert images into NumPy arrays
I_np_gray = I_gray.numpy()
I_np_rgba = I_rgba.numpy()


# Display in singseparate windows using Matplotlib
# grayscale image
plt.imshow(I_np_gray, cmap="gray", vmin=0, vmax=255)
plt.axis('off')
plt.title("Grayscale image")
plt.show()

# RGBa image
plt.imshow(I_np_rgba)
plt.axis('off')
plt.title("RGBa image")
plt.show()


# Display using Matplotlib
fig, axes = plt.subplots(1, 2)

# grayscale image
axes[0].set_title("Grayscale image")
axes[0].axis('off')
axes[0].imshow(I_np_gray, interpolation='nearest', cmap="gray", vmin=0, vmax=255)

# RGBa image
axes[1].set_title("RGBa image")
axes[1].axis('off')
axes[1].imshow(I_np_rgba, interpolation='nearest')

plt.show()