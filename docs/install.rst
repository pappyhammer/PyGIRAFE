------------
Dependencies
------------

PyCICADA has the following minimum requirements, which must be installed before you can get started using PyNWB.

#. Python 3.6, or 3.7
#. pip

PyCICADA has been tested on Ubuntu 18.04.1 LTS, Windows 10 and macOS Mojave, using Python 3.6 & 3.7

------------
Installation
------------

Install release from PyPI or from gitlab
-------------------------

1- Download cicada updated requirements from `here <https://gitlab.com/cossartlab/cicada/-/blob/master/cicada_updated_requirements.txt>`_,
open an anaconda prompt / command prompt and change directories to where the cicada_updated_requirements is

2- Create an environment and install cicada dependencies:

.. code::

    conda create -n cicada_env python=3.6.7
    conda activate cicada_env
    conda install shapely
    conda install -c conda-forge fa2
    pip install -r cicada_updated_requirements.txt
    pip install pandas==0.24.2
    pip install seaborn==0.9.0

3a- To install or update PyCICADA distribution from PyPI (not recommended, this version needs updates) run:

.. code::

    pip install -U pycicada

3b- To install the latest version CICADA from gitlab (recommended) run:

.. code::

    pip install git+https://gitlab.com/cossartlab/cicada.git


Follow the latest updates
------------

CICADA is under active development in the lab, if you have already installed CICADA and want to be sure you are using the latest version of the code, run the following:

.. code::

    conda activate cicada_env
    pip uninstall pycicada
    pip install git+https://gitlab.com/cossartlab/cicada.git

----------
How to run
----------

To run CICADA from PyPI or gitalb installation execute :

.. code::

    conda activate cicada_env
    python -m cicada

----------
Download cicada codes
----------

- To download the codes, clone CICADA:

.. code::

    cd 'path_to_where_to_clone'
    git clone https://gitlab.com/cossartlab/cicada.git

To run CICADA from the gitlab clone: 

run the '__main__.py' file from 'path_to_where_to_clone/cicada/src/cicada/__main__.py' 

- Option 1 : run (in a conda prompt)

.. code::

    conda activate cicada_env
    cd 'path_to_where_to_clone/cicada/src/cicada
    conda-develop 'path_to_where_to_clone/cicada/src
    python __main__.py


- Option 2 : example given for PyCharm users

1/ Create a Python interpreter from an existing conda environment selecting the python.exe in the cicada_env folder from the 'envs' folder:
    
    Go to settings, show all interpreters, click on '+', select 'Conda Environment', 'Existing environment', select the python interpreter (python.exe from cicada_env)


2/ Add 'path_to_where_to_clone/cicada/src' to the interpreter paths:
    
    Go to settings, show all interpreters, select the one just created, click on the folders logo ('Show paths for the selected interpreter'),  click on '+', select the 'src' folder from cicada


3/ Create a new configuration to execute the '__main__.py' file:
 
    In script path select : 'path_to_where_to_clone/cicada/src/cicada/__main__.py' for the python interpreter select the one added before


4/ Run
