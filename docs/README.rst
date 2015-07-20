.. RoNeX documentation master file, created by
   sphinx-quickstart on Thu Jun  4 08:49:35 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

RoNeX
=====

.. toctree::
   :maxdepth: 2
   :glob:
   :hidden:

   General/General-RoNeX-Setup
   GIO/GIO-Module-Manual
   SPI/SPI-Module-Manual
   Special/Special-Use-Cases


RoNeX is an industrial strength fieldbus for robots, that allows you to
connect laptops, workstations or server farms directly to your hardware,
in real time. To find out more, head over to the `RoNeX Homepage <http://www.shadowrobot.com/products/ronex>`__.

This wiki contains RoNeX documentation. Please click on one of the links
below to get started. If you can't find the information you are looking
for, `please let us
know <https://github.com/shadow-robot/sr-ronex/issues?state=open>`__!

RoNeX user support, feedback and discussions in our Google Groups based
forum `RoNeX Sig <https://groups.google.com/forum/#!forum/ronex-sig>`__.

.. image:: imgs/RoNeX.jpg
    :scale: 50%
    :align: center

:doc:`General RoNeX Setup </General/General-RoNeX-Setup>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section explains how to get started with a RoNeX system, including
setting up your computer, launching the drivers and a run through
overall layout of the system. This information is universal, regardless
of which functional modules you are using.


:doc:`GIO Module Manual </GIO/GIO-Module-Manual>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section will tell you everything you need to know to get started
with a GIO module, including the interfaces provided and various ways to
interact with the module through said interfaces.

:doc:`SPI Module Manual </SPI/SPI-Module-Manual>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section will tell you everything you need to know to get started
with an SPI module, including the interfaces provided and various ways
to interact with the module through said interfaces.


:doc:`Special Use Cases </Special/Special-Use-Cases>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section explains how to use RoNeX in non standard ways, such as
through a virtual machine, on an ARM device or through MATLAB.

`Purchase RoNeX <http://store.shadowrobot.com>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you don't already have RoNeX hardware, you can head over to our
`Online Shop <http://store.shadowrobot.com>`__ to buy it now!

EtherCAT Conformant
~~~~~~~~~~~~~~~~~~~

Although there are plans to make RoNeX etherCAT conformant, it is not
yet the case. This means that RoNeX doesn't work with programs like
TwinCAT.
