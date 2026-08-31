#https://visp-doc.inria.fr/doxygen/visp-3.7.0/tutorial-image-display-overlay.html

import sys

# ViSP Python bindings
from visp.core import ImageRGBa
from visp.core import Display
from visp.core import IoTools
from visp.core import ImagePoint
from visp.core import MouseButton
from visp.core import Font
from visp.core import Color
from visp.core import sleepMs
from visp.io import ImageIo
from visp.python.display_utils import get_display

if len(sys.argv) != 2:
    print("Usage : " + str(sys.argv[0]) + " <image name.[pgm,ppm,jpeg,png,tiff,bmp,ras,jp2]>\n")
    sys.exit()

# Reading the image
I = ImageRGBa()
try:
    ImageIo.read(I, sys.argv[1])
except:
    print("Cannot read image \"" + sys.argv[1] + "\"")
    sys.exit()

# Drawing the image
d = get_display()
d.init(I)
Display.setTitle(I, IoTools.getName(sys.argv[1]))
Display.display(I)
Display.flush(I)

print("Right click to quit")
print("Left click to inspect pixel position (i,j) and RGBa values\n")

quit = False
ip = ImagePoint()
button = MouseButton.MouseButtonType(0)
scale_factor = d.getDownScalingFactor()
font = Font(14, Font.FontFamily.GENERIC_MONOSPACE)

while not quit:
    if Display.getClick(I, ip, button, False):
        if button == MouseButton.button3:
            sys.exit()
            
        else:
            # Getting pixel coordonates
            i = int(ip.get_i())
            j = int(ip.get_j())
            ss = str(i) + " " +str(j) + ": " + str(I[i][j])
            print(ss)

            # Drawing the image with text
            font.drawText(I, ss, ImagePoint(I.getHeight() - 20*scale_factor, 10), Color.red, Color.white)
            Display.display(I)
            Display.flush(I)

    sleepMs(40)