# ViSP Python bindings
from visp.core import ImageGray
from visp.core import ImageDraw, ImagePoint
from visp.core import Display
from visp.python.display_utils import get_display


I = ImageGray(108, 192, 255)

# Draw a point
ip = ImagePoint(100, 200)
ImageDraw.drawPoint(I, ip, 0, 2)

ip1 = ImagePoint(100, 200)
ip2 = ImagePoint(300, 400)
ImageDraw.drawLine(I, ip1, ip2, Color.red, 3)