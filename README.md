How to use pyo on the BeagleBone Black with the Bela cape
=========================================================

This tutorial has been tested with a board flashed with the 
Bela image _v0.1 stable 2016.06.27_ and the latest Bela 
sources from the github repo dated June 28, 2016.

For instructions on how to flash your board, see the Bela 
wiki:

[https://github.com/BelaPlatform/Bela/wiki/Manage-your-SD-card#flashing-an-sd-card](https://github.com/BelaPlatform/Bela/wiki/Manage-your-SD-card#flashing-an-sd-card)

Step 1 - Clone or download the needed repos from github
-------------------------------------------------------

You will need three repos to run pyo projects with Bela.

- Bela: Core code and mandatory stuff to communicate with the board.

    https://github.com/BelaPlatform/Bela

- Pyo: The DSP library source code to compile on the board.

    https://github.com/belangeo/pyo

- Pyo-bela: Interface pyo/bela and pyo-project template.

    https://github.com/belangeo/pyo-bela

The next steps assumes that the three repositories are side-by-side
in the same directory (called "src" in the following example) and
that the board is plugged to the host computer with a usb cable.

Step 2 - Compile pyo on the board
---------------------------------

Copy pyo sources to the board (from the folder "src"):

    scp -r pyo/ root@192.168.7.2:/root

Connect to the board via ssh:

    ssh root@192.168.7.2

Compile pyo (the prompt should now looks like _root@bela ~$_):

    cd pyo
    sudo python setup.py install --minimal

The last step should take about 15 minutes to complete.

Step 3 - Prepare the host for managing a pyo-project
----------------------------------------------------

Back to the host computer (call exit from the ssh session or open
a new terminal window), copy the pyo-bela/build_pyo.sh script to
Bela/scripts folder and make it executable:

    cp pyo-bela/build_pyo.sh Bela/scripts
    chmod +x Bela/scripts/build_pyo.sh

Step 4 - Compile and run a pyo-project
--------------------------------------

From Bela/scripts folder, compile and run the default pyo-project:

    cd Bela/scripts
    ./build_pyo.sh ../../pyo-bela/pyo-project


Step 5 - Try the examples
-------------------------

Replace the content of the file pyo-bela/pyo-project/main.py with 
the content of a file from the pyo-bela/examples folder to try 
different processes.

Documentation
=============

For a complete description of functions that can be used to communicate 
with the pyo embedded processes, see documentation comments in the file 
PyoClass.cpp.

(c) 2016 - belangeo

