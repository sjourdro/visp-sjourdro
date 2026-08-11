================================================================
Tutorial: How to display an image and basic drawings in a window 
================================================================

.. sectnum::

.. contents:: Table of Contents

Introduction
==============

.. note::

	This tutorial is a direct Python translation of this `C++ tutorial <https://visp-doc.inria.fr/doxygen/visp-3.7.0/tutorial-image-display.html>`_.

.. note::

	We assume in this tutorial that you have successfully build your first project using ViSP as 3rd party as explained in one of the `Getting started <https://visp-doc.inria.fr/doxygen/visp-python-daily/#getting-started>`_ tutorials.

In this tutorial you will learn how to display basic drawings with ViSP either on Unix-like systems (including OSX, Fedora, Ubuntu, Debian, ...) or on Windows.

Note that all the material (source code and images) described in this tutorial is part of ViSP source code (in ``tutorial/image`` folder) and could be found in https://github.com/lagadic/visp/tree/master/tutorial/image.


Create and display an image
============================

ViSP `gui module <https://visp.inria.fr/gui>`_ provides Graphical User Interfaces capabilities that allows to display an `ImageGray <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageGray.html#visp.core.ImageGray>`_ in a window. To this end you may use several optional third-party libraries which are: `X11, GDI, OpenCV, GTK, Direct3D <https://visp.inria.fr/3rdparty_gui/>`_. We recommend to use X11 on unix-like systems thanks to `DisplayX <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.gui.DisplayX.html#visp.gui.DisplayX>`_ class and GDI on Windows thanks to `vpDisplayGDI <null>`_. If none of these classes are available, you may use vpDisplayOpenCV instead.

The following example also available in tutorial-image-display.cpp shows how to create a gray level 3840x2160 image with all the pixels set to 128, and display a red circle with 200 pixel radius in the middle of the image.

.. code::

	import sys

	from visp.core import ImageGray
	from visp.core import Display
	from visp.python.display_utils import get_display

	from visp.core import ImageCircle
	from visp.core import ImagePoint
	from visp.core import Color

	#I = ImageGray(2160, 3840, 128)
	I = ImageGray(800, 800, 128)

	d = get_display()
	d.init(I)

	Display.display(I)
	Display.displayCircleStatic(I, ImageCircle(ImagePoint(I.getHeight()/2, I.getHeight()/2), 200), Color.red, True)
	Display.flush(I)
	print("A click to quit...")
	d.getClick(I)



.. literalinclude:: /examples/image/tutorial-image-display.py

  :language: python



Depending on your screen resolution you may just see a part of the image, and certainly not the full red circle. Next image shows an example of this behavior when screen resolution is less than image size: 

https://visp-doc.inria.fr/doxygen/visp-3.7.0/img-tutorial-display.png

.. image:: https://visp-doc.inria.fr/doxygen/visp-3.7.0/img-tutorial-display.png
    :alt: Image

.. note::

	An `ImageGray <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageGray.html#visp.core.ImageGray>`_ can only be associated to one display window. In the previous example, image I is associated to display d. Depending on your platform, object d is either a `DisplayX <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.gui.DisplayX.html#visp.gui.DisplayX>`_, a `vpDisplayGDI <null>`_, a `DisplayOpenCV <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.gui.DisplayOpenCV.html#visp.gui.DisplayOpenCV>`_, a `vpDisplayGTK <null>`_ or a `vpDisplayD3D <null>`_.

Display an image larger than screen resolution
===============================================

.. note::
	Missing feature :
	VISP_DEFAULT_DISPLAY_PREFERENCE : incomplete

Manual down scaling factor
--------------------------

Auto down scaling factor
-----------------------------

Next tutorial
===============

You are now ready to see the `Tutorial: Image frame grabbing <null>`_ or `Tutorial: Image filtering <null>`_. 


