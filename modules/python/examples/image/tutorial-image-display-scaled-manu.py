#https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-image-display-scaled-manu_8cpp_source.html

import sys

# ViSP Python bindings
from visp.core import ImageGray
from visp.core import Display
from visp.core import ImageCircle
from visp.core import ImagePoint
from visp.core import Color
from visp.python.display_utils import get_display

# Creating a gray image
I = ImageGray(2160, 3840, 128)
d = get_display()
d.setDownScalingFactor(Display.SCALE_5)
d.init(I)

# Drawing a red circle on the image
Display.display(I)
Display.displayCircleStatic(I, ImageCircle(ImagePoint(I.getHeight()/2, I.getWidth()/2), 200), Color.red, True)
Display.flush(I)

# Waiting for user input
print("A click to quit...")
d.getClick(I)