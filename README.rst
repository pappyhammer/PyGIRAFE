========
PyGIRAFE
========

PyGIRAFE stands for Python Graphical Interface to Run Analyses Flexibly and Easily

It's a Python graphical interface aimed for facilitating the analyses of data. 

Our goal is to provide an easy-to-use GUI that allows to load your data, filter them and fine-tuned your analyses parameters. 

The analysis parameters are easy to set through our GUI and can be saved and re-used any time.
Each time, a log file and all parameters are saved to improve reproducibility.

The toolbox was designed to be flexible. Thus adding a new analysis is done easily in a plugin way.

Different formats of data can be added easily, as we used a wrapper system.

PyGIRAFE is under development. The version published is an alpha version and the documentation is still not complete.
Don't hesitate to contact us if you want more information.

--------
Overview
--------

.. image:: images/girafe_screenshot.png
    :align: center
    :alt: PyGIRAFE screenshot


**To see it in action, check this** `youtube video <https://youtu.be/xgf2RmrGVx0>`_


------------
Installation
------------


Install release from PyPI or from gitlab
-------------------------

1- To install or update PyGIRAFE distribution from PyPI (not recommended, this version needs updates) run:

.. code::

    pip install -U pygirafe

2- To install the latest version PyGIRAFE from GitHub (recommended) run:

.. code::

    pip install git+https://github.com/pappyhammer/pygirafe.git


Follow the latest updates
------------

PyGIRAFE is under active development, if you have already installed CICADA and want to be sure you are using the latest version of the code, run the following:

.. code::

    conda activate girafe_env
    pip uninstall pygirafe
    pip install git+https://github.com/pappyhammer/pygirafe.git

----------
How to run
----------

To run PyGIRAFE from PyPI or github installation execute :

.. code::

    conda activate girafe_env
    python -m girafe

----------
Download PyGIRAFE codes
----------

To download the codes, clone PyGIRAFE:

.. code::

    cd 'path_to_where_to_clone'
    git clone https://github.com/pappyhammer/pygirafe.git


-------------
Documentation
-------------

Documentation of PyGIRAFE will be soon available at this address `here <https://pygirafe.readthedocs.io/>`_.

-------------
Example cases
-------------

Test data will be soon available

--------
Contacts
--------


- Julien Denis (main developer): julien.denis3 (at) gmail.com


PyGIRAFE is an adaptation of a GUI & analyses pipeline that I developed previously, named CICADA.
It is available at this address: https://gitlab.com/cossartlab/cicada
Robin DARD, François PHILIPPE and Paul UTEZA have been participating in the developpement of CICADA.


-------
LICENSE
-------

Copyright (c) 2022 Julien DENIS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
