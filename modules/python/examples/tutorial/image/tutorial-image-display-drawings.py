# ViSP Python bindings
from visp.core import ImageGray
from visp.core import ImageDraw, ImagePoint, Rect, Font
from visp.core import Display
from visp.python.display_utils import get_display


# Create subplots for the figure
def display(I, title):
	d = get_display()
	d.init(I)
	Display.display(I)
	Display.setTitle(I, title)


# Create a black image
I = ImageGray(100, 100, 0)


# Draw a point
ip = ImagePoint(50, 50)
display(I, "Point")
Display.displayPoint(I, ip, 255, 3)
Display.flush(I)

# Draw a line
ip1 = ImagePoint(25, 25)
ip2 = ImagePoint(75, 75)
ImageDraw.drawLine(I, ip1, ip2, 255, 3)
display(I, "Line")

# Draw a circle
ip = ImagePoint(50, 50)
ImageDraw.drawCircle(I[2], ip, 40, 255, 3)
create_subplot(2, "Circle")

# Draw a rectangle
ip = ImagePoint(25, 10)
w = 80
h = 50
ImageDraw.drawRectangle(I[3], Rect(ip, w, h), 255, 3)
create_subplot(3, "Rectangle")

# Draw a cross
ip = ImagePoint(50, 50)
ImageDraw.drawCross(I[4], ip, 25, 255, 3)
create_subplot(4, "Cross")

# Insert text
ip = ImagePoint(43, 25)
color = 255 # white
background = 0 # black
font = Font(14, Font.FontFamily.GENERIC_MONOSPACE)
font.drawText(I[5], "Test...", ip, color, background)
create_subplot(5, "Text")


# Display results
plt.show()