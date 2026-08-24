import sys

# ViSP Python bindings
from visp.core import ImageGray, ImageRGBa, Color
from visp.core import Display
from visp.python.display_utils import get_display


# Create ViSP images
I_gray = ImageGray(800, 800, 125)		# grayscale image
I_rgba = ImageRGBa(800, 800, Color.red)	# RGBa image


# Display using ViSP
# grayscale image
d = get_display()
d.init(I_gray)
Display.setTitle(I_gray, "Grayscale image")
Display.display(I_gray)
Display.flush(I_gray)

# Wait for user input
print("A click to quit...")
Display.getClick(I_gray)


# RGBa image
d.init(I_rgba)
Display.setTitle(I_rgba, "RGBa image")
Display.display(I_rgba)
Display.flush(I_rgba)

# Wait for user input
print("A click to quit...")
Display.getClick(I_rgba)
