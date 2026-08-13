==========================================================
Tutorial: How to modify an image to insert basic drawings
==========================================================

.. sectnum::

.. contents:: Table of Contents

Introduction
============

.. note::

	This tutorial is a direct Python translation of this `C++ tutorial <https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-basic-drawings.html>`_.

In this tutorial you will learn how to modify the content of an image adding basic drawings without the need of an image display window. This functionality could be useful if none of the following 3rd parties are available: `X11, GDI, OpenCV, GTK, Direct3D <https://visp.inria.fr/3rdparty_gui/>`_.

Modify an image with basic drawings
===================================

There is the `ImageDraw <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageDraw.html#visp.core.ImageDraw>`_ class that allows to modify an image by inserting basic drawings like point, circle, line, rectangle, polygon, frame. There is also `Font <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Font.html#visp.core.Font>`_ class that allows to modify an image to insert text. These classes are used in `testImageDraw.py <none>`_.

If you run the corresponding binary: 

.. code::
	:language: bash

	$ cd $VISP_WS/visp-build/modules/core
	$ ./testImageDraw

it will create ``canvas_color.png`` and ``canvas_gray.png`` images that give a good overview.

* Content of ``canvas_color.png`` image that shows basic drawings inserted in a color image implemented as an `ImageRGBa <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageRGBa.html#visp.core.ImageRGBa>`_ is the following: 


.. image:: https://visp-doc.inria.fr/doxygen/visp-daily/img-tutorial-drawings-color.png
    :alt: Image

* Content of ``canvas_gray.png`` image that shows basic drawings inserted in a gray level image implemented as a `ImageGray <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageGray.html#visp.core.ImageGray>`_ is the following: 

.. image:: https://visp-doc.inria.fr/doxygen/visp-daily/img-tutorial-drawings-gray.png
    :alt: Image

Draw a point in an image
-----------------------------

The following snippet shows how to modify color image I drawing a red point at pixel location (100, 200).


.. code::
	:language: python

	I = ImageRGBa(480, 640)
	ip = ImagePoint(100, 200)
	ImageDraw.drawPoint(I, ip, Color.red, 2)

The following snippet shows how to modify a gray level image I drawing a white point at pixel location (100, 200).

.. code::
	:language: python

	I = ImageGray(480, 640)
	ip = ImagePoint(100, 200)
	color = 255 # white
	ImageDraw.drawPoint(I, ip, color, 2)

Draw a line
--------------------

The following snippet shows how to modify color image I drawing an orange line with thickness 3 between pixels with coordinates (100, 200) and (300, 400).

.. code::
	:language: python

	I = ImageRGBa(480, 640)
	ip1 = ImagePoint(100, 200)
	ip2 = ImagePoint(300, 400)
	ImageDraw.drawLine(I, ip1, ip2, Color.red, 3)

The following snippet shows how to modify gray level image I drawing a black line with thickness 3 between pixels with coordinates (100, 200) and (300, 400).

.. code::
	:language: python

	I = ImageGray(480, 640)
	ip1 = ImagePoint(100, 200)
	ip2 = ImagePoint(300, 400)
	color = 0 # black
	ImageDraw.drawLine(I, ip1, ip2, color, 3)

Draw a circle
-------------------

The following snippet shows how to modify color image I drawing a green cercle with thickness 3, centered at pixel location (100, 200) and with radius 80 pixels.

.. code::
	:language: python

	I = ImageRGBa(480, 640)
	ip = ImagePoint(100, 200)
	ImageDraw.drawCircle(I, ip, 80, Color.green, 3)

The following snippet shows how to modify gray level image I drawing a gray cercle with thickness 3, centered at pixel location (100, 200) and with radius 80 pixels.

.. code::
	:language: python

	I = ImageGray(480, 640)
	ip = ImagePoint(100, 200)
	color = 128 # gray
	ImageDraw.drawCircle(I, ip, 80, color, 3)

Draw a rectangle
------------------------

The following snippet shows how to modify color image I drawing a yellow rectangle with thickness 3, with top left corner location (100, 200), and rectangle width and height set to 150, 80 respectively.

.. code::
	:language: python

	I = ImageRGBa(480, 640)
	ip = ImagePoint(100, 200)
	w = 150
	h = 80
	ImageDraw.drawRectangle(I, Rect(ip, w, h), Color.yellow, 3)

The following snippet shows how to modify gray level image I drawing a light gray rectangle with thickness 3, with top left corner location (100, 200), and rectangle width and height set to 150, 80 respectively.

.. code::
	:language: python

	I = ImageGray(480, 640)
	ip = ImagePoint(100, 200)
	w = 150
	h = 80
	color = 200 # light gray
	ImageDraw.drawRectangle(I, Rect(ip, w, h), color, 3)

Draw a cross
--------------------

The following snippet shows how to modify color image I drawing a blue cross with thickness 3, location (100, 200), and size 15 pixels.

.. code::
	:language: python

	I = ImageRGBa(480, 640)
	ip = ImagePoint(100, 200)
	ImageDraw.drawCross(I, ip, 15, Color.blue, 3)

The following snippet shows how to modify gray level image I drawing a dark gray cross with thickness 3, location (100, 200), and size 15 pixels.

.. code::
	:language: python

	I = ImageGray(480, 640)
	ip = ImagePoint(100, 200)
	color = 50 # dark gray
	ImageDraw.drawCross(I, ip, 15, color, 3)

Insert text in an image
----------------------------

The following snippet shows how to modify color image I drawing "Hello world" in white over a black background at location (100, 200).


.. code::
	:language: python

	I = ImageRGBa(480, 640)
	ip = ImagePoint(100, 200)
	font = Font(14, Font.FontFamily.GENERIC_MONOSPACE)
	font.drawText(I, "Test...", ip, Color.white, Color.black)

The following snippet shows how to modify gray level image I drawing "Hello world" in white over a black background at location (100, 200).


.. code::
	:language: python

	I = ImageGray(480, 640)
	ip = ImagePoint(100, 200)
	color = 255 # white
	background = 0 # black
	font = Font(14, Font.FontFamily.GENERIC_MONOSPACE)
	font.drawText(I, "Test...", ip, color, background)


Next tutorial
================

You are now ready to see how to continue with `Tutorial: Image frame grabbing <none>`_. 