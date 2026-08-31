#https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-draw-rectangle_8cpp_source.html

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

# Drawing a red rectangle on the image
Display.display(I)
Display.displayRectangle(I, ImagePoint(I.getHeight()/4, I.getWidth()/4), ImagePoint(I.getHeight()*3/4, I.getWidth()*3/4), Color.red, True)
Display.flush(I)

# Waiting for user input
print("A click to quit...")
Display.getClick(I)