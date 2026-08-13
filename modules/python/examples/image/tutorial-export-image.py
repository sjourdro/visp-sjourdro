#https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-export-image_8cpp_source.html

# ViSP Python bindings
from visp.core import ImageGray
from visp.core import ImageRGBa
from visp.core import Display
from visp.core import ImagePoint
from visp.core import Color
from visp.io import ImageIo
from visp.python.display_utils import get_display

# Creating a gray image
I = ImageGray(240, 320, 255)
Ioverlay = ImageRGBa()
d = get_display()
d.setDownScalingFactor(Display.SCALE_AUTO)
d.init(I)
Display.setTitle(I, "Save overlayed image")

# Drawing a rectangle on the image
Display.display(I)
Display.displayRectangle(I, ImagePoint(10, 10), 100, 10, Color.red, True)
Display.flush(I)

# Saving the image
Display.getImage(I, Ioverlay)
ofilename = "overlay.png"
print("Save overlayed image in: " + str(ofilename))
ImageIo.write(I, ofilename)

# Waiting for user input
print("A click to quit...")
Display.getClick(I)