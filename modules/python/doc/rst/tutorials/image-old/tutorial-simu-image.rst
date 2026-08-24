=================================
Tutorial: Planar image projection
=================================

Introduction
==============

.. note::

	This tutorial is a direct Python translation of this `C++ tutorial <https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-simu-image.html>`_.

The aim of this tutorial is to explain how to use `ImageSimulator <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.robot.ImageSimulator.html#visp.robot.ImageSimulator>`_ class to project an image of a planar scene at a given camera position. For example, this capability can then be used during the simulation of a visual-servo as described in `Tutorial: Image-based visual servo (IBVS) <https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-ibvs.html>`_ to introduce an image processing.

Note that all the material (source code and images) described in this tutorial is part of ViSP source code (in ``simulator/image`` folder) and could be found in https://github.com/lagadic/visp/tree/master/simulator/image.

Image projection
================

Given the image of a planar 20cm by 20cm square target as the one presented in the next image, we show here after how to project this image at a given camera position, and how to get the resulting image.


.. image:: https://visp-doc.inria.fr/doxygen/visp-daily/img-target-square.png
	:alt: image
	:align: center

Image of a planar 20cm by 20cm square target.

This is done by the following code also available in `tutorial-image-simulator.cpp <none>`_: 

.. literalinclude:: /examples/simulator/tutorial-image-simulator.py
	:language: python
	:linenos:
	:lines: 3-


The result of this program is shown in the next image.


.. image:: https://visp-doc.inria.fr/doxygen/visp-daily/img-simu-image-target-square.jpg
	:alt: image
	:align: center

Resulting projection of the planar image at a given camera position.



The provide hereafter the explanation of the new lines that were introduced.

.. code-block:: python

	from visp.robot import ImageSimulator

Include the header of the `ImageSimulator <https://visp-doc.inria.fr/doxygen/visp-python-daily/_autosummary/visp.robot.ImageSimulator.html#visp.robot.ImageSimulator>`_ class that allows to project an image to a given camera position.

Then in the main() function we create an instance of a gray level image that corresponds to the image of the planar target, and then we read the image from the disk.

.. code-block:: python

	target = ImageGray()
	ImageIo.read(target, "target_square.jpg")

Since the previous image corresponds to a 20cm by 20cm target, we initialize the 3D coordinates of each corner in the plane Z=0. Each

.. code-block:: python

	p1 = Point(-0.1, -0.1, 0.0) # Top left
	p2 = Point(0.1, -0.1, 0.0) # Top right
	p3 = Point(0.1, 0.1, 0.0) # Bottom right
	p4 = Point(-0.1, 0.1, 0.0) # Bottom left
	X = [p1, p2, p3, p4]

Then we create an instance of the image ``I`` that will contain the rendered image from a given camera position.

.. code-block:: python

	I = ImageGray(480, 640)

Since the projection depends on the camera, we set its intrinsic parameters.

.. code-block:: python

	cam = CameraParameters(840, 840, I.getWidth() / 2, I.getHeight() / 2)

We also set the render position of the camera as an homogeneous transformation between the camera frame and the target frame.


.. code-block:: python

	cMo = HomogeneousMatrix(0.0, 0.0, 0.35, 0.0, math.radians(30.0), math.radians(15.0))

We create here an instance of the planar image projector, set the interpolation to bilinear and initialize the projector with the image of the target and the coordinates of its corners.


.. code-block:: python

	sim = ImageSimulator()
    sim.setInterpolationType(ImageSimulator.BILINEAR_INTERPOLATION)
    sim.init(target, X)

Now to retrieve the rendered image we first clean the content of the image to render, set the camera position, and finally get the image using the camera parameters.

.. code-block:: python

	sim.setCleanPreviousImage(True)
    sim.setCameraPosition(cMo)
    sim.getImage(I, cam)

Then, if ``libjpeg`` is available, the rendered image is saved in the same directory then the executable.

.. code-block:: python

    try {
    	vpImageIo::write(I, "./rendered_image.jpg");
    }
    catch (...) {
    	std::cout << "Unsupported image format" << std::endl;
    }

Finally, as in `Tutorial: How to create and build a project that uses ViSP and CMake on Unix or Windows <https://visp-doc.inria.fr/doxygen/visp-daily/tutorial-getting-started.html>`_ we open a window to display the rendered image.

Note that this planar image projection capability has been also introduced in `VirtualGrabber <none>`_ class exploited in `tutorial-ibvs-4pts-image-tracking.cpp <none>`_. Thus the next `Tutorial: Image-based visual servo (IBVS) <none>`_ shows how to use it in order to introduce an image processing that does the tracking of the target during a visual-servo simulation. 

