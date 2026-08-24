=============================================
Getting Started
=============================================

.. contents:: Table of contents :

Introduction
============

.. warning::

	This tutorial is still in drafting phase and may contain errors.

.. note::

	We assume in this tutorial that you have successfully installed and configured ViSP with Python bindings as explained in this `ViSP building tutorial <https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-install-python-bindings.html>`_.

In this tutorial you will learn how to :
 * Create an image (using  `ImageGray <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageGray.html#visp.core.ImageGray>`_ and `ImageRGBa <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageRGBa.html#visp.core.ImageRGBa>`_)
 * Display an image in a ViSP window (using `Display <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display>`_)
 * Display an image in a Matplotlib figure (using NumPy conversion)
 * Read and write an image from and to a file (using `ImageIo <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.io.ImageIo.html#visp.io.ImageIo.read>`_)



.. note::

	All the material (source code and images) described in this tutorial is part of ViSP source code (in ``tutorial/image`` folder) and could be found in `https://github.com/lagadic/visp/tree/master/modules/python/tutorial/image <none>`_.

Create an image
===============

ViSP disposes of various image classes to represent different pixel representations.
We will show here how to create a grayscale image using the `ImageGray <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageGray.html#visp.core.ImageGray>`_ class and a color image using the `ImageRGBa <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageRGBa.html#visp.core.ImageRGBa>`_ class.

.. note::

	All image classes (including `ImageGray <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageGray.html#visp.core.ImageGray>`_ and `ImageRGBa <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.ImageRGBa.html#visp.core.ImageRGBa>`_) are bindings from the generic C++ class `vpImage\<Type\> <https://visp-doc.inria.fr/doxygen/visp-daily/classvpImage.html>`_, with "Type" the type of the image's pixels, and therefore share the same methods and operators.




Grayscale image
---------------

To create an empty grayscale image, you can call the class constructor :

.. code-block:: python

	I_gray = ImageGray()

You can specify the image dimensions, as well as a default pixel value, using the corresponding arguments.
Here is the creation of a square image with a length of 800 pixels, with a pixel value of 125, wich correspond to gray:

.. code-block:: python

	I_gray = ImageGray(800, 800, 125)

RGBa image
----------

You can create a RGBa image the same way as a grayscale image :

.. code-block:: python

	I_rgba = ImageRGBa()

To assign it a pixel value, you will need to use the `Color <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Color.html#visp.core.Color>`_ class.
It contains various default color to use. For example, here is the creation of a red image :

.. code-block:: python

	I_rgba = ImageRGBa(800, 800, Color.red)

You can also set your own color by entering its RGBa (Red, Green, Blue, alpha = opacity) values :


.. code-block:: python

	I_rgba = ImageRGBa(800, 800, Color(255, 0, 0, 255, Color.ColorIdentifier.id_red))



Display an image
================

ViSP disposes of its own way of displaying images inherited from its C++ version. This said, Matplotlib is a popular Python module for displaying images and figures, and you may be interested in it.
This is why we will see both options in this tutorial.

Using ViSP
----------

.. note::

	h

The `Display <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.core.Display.html#visp.core.Display>`_ class can be used to display an image in a window.
You will first need to create a Display object using the `get_display() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.display_utils.get_display.html#visp.display_utils.get_display>`_ method from the visp.core.display_utils module, and initialize it with the image :

.. code-block:: python

	d = get_display()
	d.init(I)

Then display it with :

.. code-block:: python

	Display.display(I)
	Display.flush(I)

The following example creates both an ImageGray and an ImageRGBa objects, and displays the two of them in separate windows :

.. literalinclude:: /examples/tutorial/image/tutorial-image-display-visp.py
	:language: python
	:linenos:

Using Matplotlib
----------------

.. note::

	To use this option, you need to have installed NumPy and Matplotlib modules in your Python environment.

ViSP images can be converted into a NumPy array using the numpy() method of ViSP image classes :

.. code-block:: python

	I_numpy = I_visp.numpy()

The newly created NumPy array can then be displayed in a Matplotlib plot :

.. code-block:: python

	plt.imshow(I_numpy)
	plt.show()

.. important::

	In case of a grayscale image, you will need to use the "cmap='gray', vmin=0, vmax=255" arguments in the plt.imshow() method for it to be displayed properly.

The following exemple creates both an ImageGray and an ImageRGBa objects, and displays the two of them first in separate figures then in the same figure :

.. literalinclude:: /examples/tutorial/image/tutorial-image-display-visp.py
	:language: python
	:linenos:

.. hint::
	You can also initialize a ViSP image with a NumPy image.

I/O operations
==============

The `ImageIo <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.io.ImageIo.html#visp.io.ImageIo.read>`_ class come with methods to both import and save an image file as an image object.
It can interact with .pgm, .ppm, .jpeg, .png, .tiff, .bmp, .ras and .jp2 files.

Read an image
-------------

To read an image, use the `read() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.io.ImageIo.html#visp.io.ImageIo.read>`_ method while specifying the file path :

.. code-block:: python

	ImageIo.read(I, path)

Write an image
--------------

To write an image, use the `write() <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.io.ImageIo.html#visp.io.ImageIo.write>`_ method while specifying the file path :

.. code-block:: python

	ImageIo.write(I, path)

The following exemple opens the file ``monkey.jpeg``, display it, and save it under a different name :

.. literalinclude:: /examples/tutorial/image/tutorial-image-io.py
	:language: python
	:linenos: