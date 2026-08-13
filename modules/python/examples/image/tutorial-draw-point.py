#https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-draw-point_8cpp_source.html

from visp.core import ImageGray
from visp.core import Display
from visp.core import ImagePoint
from visp.core import Color
from visp.python.display_utils import get_display

# Creating a gray image
I = ImageGray(2160, 3840, 128)
#I = ImageGray(800, 800, 128)
d = get_display()
d.setDownScalingFactor(Display.SCALE_AUTO)
d.init(I)
Display.setTitle(I, "Point drawing")

# Drawing a red point on the image
Display.display(I)
Display.displayPoint(I, ImagePoint(I.getHeight()/2, I.getWidth()/2), Color.red, 2)
Display.flush(I)

# Waiting for user input
print("A click to quit...")
Display.getClick(I)