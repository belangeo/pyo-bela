How to use pyo on the BeagleBone Black with bela
================================================ 

------------------------------------------------------------------------
------------------------------------------------------------------------
Step 1 - Changes made to the image bela\_stable\_2016.04.19.img

1) Need the python-dev package

    sudo apt-get install python-dev

2) Compile a minimalistic pyo (libsndfile as only dependency)

    git -c http.sslVerify=false clone https://github.com/belangeo/pyo.git
    cd pyo
    sudo python setup.py install --minimal

3) Modify the Makefile to compile and link with python

line 11:
    
    LIBS := -lrt -lnative -lxenomai -lsndfile `python-config --ldflags`

line 20:
    
    CPP_FLAGS := -O3 -march=armv7-a -mtune=cortex-a8 -mfloat-abi=hard -mfpu=neon -ftree-vectorize `python-config --cflags`

------------------------------------------------------------------------
------------------------------------------------------------------------
Step 2 - On the host computer, clone the beaglert repository:
    
    hg clone https://code.soundsoftware.ac.uk/hg/beaglert

------------------------------------------------------------------------
------------------------------------------------------------------------
Step 3 - Copy the folder "pyo-project" in the beaglert/projects directory 
or give the full path of the folder in step 4.

------------------------------------------------------------------------
------------------------------------------------------------------------
Step 4 - From the script folder, with the BBB plugged to the host computer,
compile and run your project:
    
    ./build_project.sh ../projects/pyo-project

See the bela wiki for more options when building projects on the BBB board.

https://code.soundsoftware.ac.uk/projects/beaglert/wiki/\_Compiling\_Bela\_projects\_on\_the\_board

------------------------------------------------------------------------
------------------------------------------------------------------------
Step 5 - Replace the content of the file "main.py" with the content of an
example from the examples folder to try different processes.

Documentation
=============

For a complete description of functions that can be used to communicate 
with the pyo embedded processes, see documentation comments in the file 
PyoClass.cpp.

(c) 2016 - belangeo

