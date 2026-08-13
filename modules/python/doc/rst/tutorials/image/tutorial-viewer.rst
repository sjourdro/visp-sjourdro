=================================================================
Tutorial: How to display an image and basic drawings in a window
=================================================================


.. sectnum::

.. contents:: Table of Contents



Introduction
==============

.. note::

	This tutorial is a direct Python translation of this `C++ tutorial <https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-image-display-overlay.html>`_.

In this tutorial you will learn how to display basic drawings with ViSP either on Unix-like systems (including OSX, Fedora, Ubuntu, Debian, ...) or on Windows.

Note that all the material (source code and images) described in this tutorial is part of ViSP source code (in ``tutorial/image`` folder) and could be found in https://github.com/lagadic/visp/tree/master/tutorial/image.


Load and display an image
===========================

ViSP `gui module <https://visp.inria.fr/gui>`_ provides Graphical User Interfaces capabilities that allows to display an `ImageGray <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageGray.html#visp.core.ImageGray>`_ in a window. To this end you may use several optional third-party libraries which are: `X11, GDI, OpenCV, GTK, Direct3D <https://visp.inria.fr/3rdparty_gui/>`_. We recommend to use X11 on unix-like systems thanks to `DisplayX <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.gui.DisplayX.html#visp.gui.DisplayX>`_ class and GDI on Windows thanks to `vpDisplayGDI <null>`. If none of these classes are available, you may use `DisplayOpenCV <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.gui.DisplayOpenCV.html>`_ instead.

The following example also available in tutorial-image-display.cpp shows how to create a gray level 3840x2160 image with all the pixels set to 128, and display a red circle with 200 pixel radius in the middle of the image.



.. literalinclude:: /examples/image/tutorial-viewer.py
	:language: python



Once build, if you run the corresponding binary ``loading monkey.jpeg`` image:

.. code::
	:language: bash

	$ cd $VISP_WS/visp-build/tutorial/image
	$ ./tutorial-viewer monkey.jpeg

It will open a window containing ``loading monkey.jpeg`` image: 

.. image:: https://visp-doc.inria.fr/doxygen/visp-daily/img-monkey.jpg
    :alt: Image

A detailed explanation of the source is available following 2.2. Get `tutorial-viewer.cpp <https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-getting-started.html#tutorial_viewer_code>`_ file section.


Display basic drawings in window overlay
=========================================

There are a lot of examples in ViSP that show how to display drawings in window overlay. There is `testDisplays.cpp <https://visp-doc.inria.fr/doxygen/visp-daily/testDisplays_8cpp_source.html>`_ that gives an overview.

If you run the corresponding binary: 

.. code::
	:language: bash

	$ cd $VISP_WS/visp-build/modules/gui
	$ ./testDisplays

it will open a window like the following: 

.. image:: https://visp-doc.inria.fr/doxygen/visp-daily/img-tutorial-display-drawings.png
    :alt: Image

Display a point in overlay
---------------------------


As shown in `tutorial-draw-point.py <none>`_ which source code is given below we use `Display.displayPoint() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display.displayPoint>`_ function to draw a point in the overlay of a windows that displays a 3840 by 2160 grey image that has all the pixels set to 128 gray level.

.. code::
	:language: python

	Display.displayPoint(I, ImagePoint(I.getHeight()/2, I.getWidth()/2), Color.red, 2)

Here we draw a point at the center of a grey image with red color and thickness 2.

Display a line between 2 points in overlay
------------------------------------------

As given in `tutorial-draw-line.py <none>`_ we use `Display.displayLine() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display.displayLines>`_ function to draw a line segment on the screen.

.. code::
	:language: python

	Display.displayLine(I, ImagePoint(I.getHeight()/4, I.getWidth()/4), ImagePoint(I.getHeight()*3/4, I.getWidth()*3/4), Color.red, 10)

Here we draw a red coloured line segment with the specified initial and final coordinates and thickness 10.

Display a circle in overlay
---------------------------

As given in `tutorial-image-display-scaled-auto.py <none>`_ we use `Display.displayCircleStatic() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display.displayCircleStatic>`_ function to draw a circle on the screen.

.. code::
	:language: python

	Display.displayCircleStatic(I, ImageCircle(ImagePoint(I.getHeight()/2, I.getWidth()/2), 200), Color.red, True)

Here we draw a red coloured filled circle at the center with radius of 200.

Display a rectangle in overlay
------------------------------

As given in `tutorial-draw-rectangle.py <none>`_ we use `Display.displayRectangle() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display.displayRectangle>`_ function to draw a rectangle on the screen.

.. code::
	:language: python

	Display.displayRectangle(I, ImagePoint(I.getHeight()/4, I.getWidth()/4), ImagePoint(I.getHeight()*3/4, I.getWidth()*3/4), Color.red, True)

Here we draw a red coloured filled rectangle with specified top-left coordinates and width and height. 

Display a cross in overlay
--------------------------

As given in `tutorial-draw-cross.py <none>`_ we use `Display.displayCross() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display.displayCross>`_ function to draw a rectangle on the screen.

.. code::
	:language: python

	Display.displayCross(I, ImagePoint(I.getHeight()/2, I.getWidth()/2), int(I.getWidth()/2), Color.red, 2)

Here we draw a red coloured cross on the center with speicfied size and thickness 2.

Display text in window overlay
------------------------------

As given in `tutorial-draw-text.py <none>`_ we use `Display.displayText() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display.displayText>`_ function to add text in the window overlay.

.. code::
	:language: python

	Display.displayText(I, ImagePoint(I.getHeight()/2, I.getWidth()/2), "Hello World!", Color.yellow)

Here ``Hello world`` is displayed in the middle of the image.

Export and save the content of a window as an image
===================================================

As given in `tutorial-export-image.py <none>`_ which source code is given below, we use `Display.getImage() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display.getImage>`_ function to export the image with the whole drawings in overlay. Then we use `ImageIo.write() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.io.ImageIo.html#visp.io.ImageIo.write>`_ to save the image in png format.

.. literalinclude:: /examples/image/tutorial-export-image.py
	:language: python


Handle keyboard events in a window
==================================

As given in `tutorial-event-keyboard.py <none>`_ which code is given below, we use `Display.getKeyboardEvent() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display.getKeyboardEvent>`_ function to get the value of the key pressed.

.. literalinclude:: /examples/image/tutorial-event-keyboard.py
	:language: python

Next tutorial
=================

You are now ready to see how to continue with `Tutorial: How to modify an image to insert basic drawings <https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-basic-drawings.html>`_. 