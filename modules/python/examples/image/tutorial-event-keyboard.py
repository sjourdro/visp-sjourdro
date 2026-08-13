#https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-event-keyboard_8cpp_source.html

# ViSP Python bindings
from visp.core import ImageGray
from visp.core import Display
from visp.core import sleepMs
from visp.python.display_utils import get_display

# Create a black image
I = ImageGray(240, 320)
d = get_display()
d.setDownScalingFactor(Display.SCALE_AUTO)
d.init(I)
Display.setTitle(I, "Keyboard event example")
Display.display(I)
Display.flush(I)

# Blocking keyboard event
print("Waiting a keyboard event...")
Display.getKeyboardEvent(I, True)
print("A keyboard event was detected")

# Non blocking keyboard event
cpt_event = 0
print("Enter a non blocking keyboard event detection loop...")
while cpt_event < 5:
    event, key = Display.getKeyboardEventWithKey(I, False)
    if event:
        print("Key detected: " + key)
        cpt_event += 1
    sleepMs(5)