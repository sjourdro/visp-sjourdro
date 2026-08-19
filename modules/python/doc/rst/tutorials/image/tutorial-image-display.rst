================================================================
Tutorial: How to display an image and basic drawings in a window 
================================================================

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

ViSP `gui module <https://visp.inria.fr/gui>`_ provides Graphical User Interfaces capabilities that allows to display an `ImageGray <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageGray.html#visp.core.ImageGray>`_ in a window. To this end you may use several optional third-party libraries which are: `X11, GDI, OpenCV, GTK, Direct3D <https://visp.inria.fr/3rdparty_gui/>`_. We recommend to use X11 on unix-like systems thanks to `DisplayX <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.gui.DisplayX.html#visp.gui.DisplayX>`_ class and GDI on Windows thanks to `vpDisplayGDI <null>`_. If none of these classes are available, you may use `DisplayOpenCV <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.gui.DisplayOpenCV.html>`_ instead.

The following example also available in `tutorial-image-display.cpp <null>`_ shows how to create a gray level 3840x2160 image with all the pixels set to 128, and display a red circle with 200 pixel radius in the middle of the image.



.. literalinclude:: /examples/image/tutorial-image-display.py
	:language: python
	:linenos:
	:lines: 3-




Depending on your screen resolution you may just see a part of the image, and certainly not the full red circle. Next image shows an example of this behavior when screen resolution is less than image size: 

.. image:: https://visp-doc.inria.fr/doxygen/visp-3.7.0/img-tutorial-display.png
	:alt: image
	:align: center

.. note::

	An `ImageGray <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageGray.html#visp.core.ImageGray>`_ can only be associated to one display window. In the previous example, image I is associated to display d. Depending on your platform, object d is either a `DisplayX <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.gui.DisplayX.html#visp.gui.DisplayX>`_, a `vpDisplayGDI <null>`_, a `DisplayOpenCV <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.gui.DisplayOpenCV.html#visp.gui.DisplayOpenCV>`_, a `vpDisplayGTK <null>`_ or a `vpDisplayD3D <null>`_.

Display an image larger than screen resolution
===============================================

Manual down scaling factor
--------------------------

This other example available in `tutorial-image-display-scaled-manu.py </examples/image/tutorial-image-display-scaled-manu.py>`_ shows how to modify the previous example in order to introduce a down scaling factor to reduce the size of the display by 5 along the lines and the columns. This feature may be useful to display images that are larger than the screen resolution.

To down scale the display size, just modify the previous example using the `Display.ScaleType <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display.ScaleType>`_ parameter to the `setDownScalingFactor() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display.setDownScalingFactor>`_ method.

.. code-block:: python

	d.setDownScalingFactor(Display.SCALE_5)
	d.init(I)

Auto down scaling factor
-----------------------------

This other example available in `tutorial-image-display-scaled-auto.py </examples/image/tutorial-image-display-scaled-auto.py>`_ shows now how to modify the previous example in order to introduce an auto down scaling factor that is automatically computed from the screen resolution in order that two images could be displayed given the screen resolution.

To consider an auto down scaling factor, modify the previous example adding the `Display.SCALE_AUTO <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display.ScaleType>`_ parameter to the `setDownScalingFactor() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display.setDownScalingFactor>`_ method.

.. code-block:: python
	
	d.setDownScalingFactor(Display.SCALE_AUTO)
	d.init(I)

Next tutorial
===============

You are now ready to see the `Tutorial: Image frame grabbing <null>`_ or `Tutorial: Image filtering <null>`_. 


