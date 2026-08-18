#https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-image-simulator_8cpp_source.html

import sys
import math

# ViSP Python bindings
from visp.core import ImageGray, Point, CameraParameters, HomogeneousMatrix
from visp.io import ImageIo
from visp.robot import ImageSimulator
from visp.core import Display
from visp.python.display_utils import get_display



def main():
    try:
        # Read image
        target = ImageGray()
        ImageIo.read(target, sys.path[0] + "/target_square.jpg")

        # Set model
        p1 = Point(-0.1, -0.1, 0.0) # Top left
        p2 = Point(0.1, -0.1, 0.0) # Top right
        p3 = Point(0.1, 0.1, 0.0) # Bottom right
        p4 = Point(-0.1, 0.1, 0.0) # Bottom left
        X = [p1, p2, p3, p4]

        # Image construction
        I = ImageGray(480, 640)

        # Camera parameters
        cam = CameraParameters(840, 840, I.getWidth() / 2, I.getHeight() / 2)

        # Set cMo (camera position)
        cMo = HomogeneousMatrix(0.0, 0.0, 0.35, 0.0, math.radians(30.0), math.radians(15.0))

        # Create simulator
        sim = ImageSimulator()
        sim.setInterpolationType(ImageSimulator.BILINEAR_INTERPOLATION)
        sim.init(target, X)

        # Get the new image of the projected planar image target
        sim.setCleanPreviousImage(True)
        sim.setCameraPosition(cMo)
        sim.getImage(I, cam)

        # Write image
        try:
            ImageIo.write(I, "./rendered_image.jpg")
        except Exception:
            print("Unsupported image format")

        # Display image
        d = get_display()
        d.init(I)
        Display.setTitle(I, "Planar image projection")
        Display.display(I)
        Display.flush(I)

        # Wait for user input
        print("A click to quit...")
        Display.getClick(I)

    except Exception as e:
        print(f"Catch an exception: {e}")



if __name__ == "__main__":
    main()