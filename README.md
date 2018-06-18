How to use pyo on the BeagleBone Black with the Bela cape
=========================================================

This tutorial has been tested with a board flashed with the 
Bela image _v0.3.4_ and the latest Bela sources from the 
github repo dated June 16, 2018.

For instructions on how to flash your board, see the Bela 
wiki:

[https://github.com/BelaPlatform/Bela/wiki/Manage-your-SD-card#flashing-an-sd-card](https://github.com/BelaPlatform/Bela/wiki/Manage-your-SD-card#flashing-an-sd-card)

Step 1 - Clone or download the needed repos from github
-------------------------------------------------------

You will need two repos to run pyo projects with Bela platform.

- Bela: Core code and mandatory stuff to communicate with the board.

    https://github.com/BelaPlatform/Bela

- Pyo-bela: Interface pyo/bela, pre-compiled binaries and project template.

    https://github.com/belangeo/pyo-bela

The next steps assumes that the two repositories are side-by-side
in the same directory and that the board is plugged to the host 
computer with a usb cable.

Step 2 - Install pyo binaries on the board
------------------------------------------

To download and install the latest pyo binaries on the board, run the 
script _install\_pyo\_on\_board.sh_ from pyo-bela sources (or follow
instructions on the [release page](https://github.com/belangeo/pyo-bela/releases)):

    cd pyo-bela
    ./install_pyo_on_board.sh

Step 3 - Prepare the host for managing a pyo-bela project
-----------------------------------------------------------

Copy the pyo-bela/build_pyo.sh script to Bela/scripts folder and make it executable:

    cp pyo-bela/build_pyo.sh Bela/scripts
    chmod +x Bela/scripts/build_pyo.sh

At this point, if you never update the board (i.e. you just flashed your sd card), you
should call the script update_board to copy the latest framework from Bela to your board:

    cd Bela/scripts
    ./update_board

Step 4 - Compile and run a pyo-bela project
-------------------------------------------

From Bela/scripts folder, compile and run any of the examples in the 
pyo-bela/examples folder. The first argument to the build_pyo.sh script is 
the python file to execute (the project will have the same name as this file, 
without ".py"). The second argument is the path of the pyo-bela/common folder,
which contain all needed files to run a bela project.

    cd Bela/scripts
    ./build_pyo.sh ../../pyo-bela/examples/music-box.py ../../pyo-bela/common

The second argument can be ommited if an environment variable called PYO_BELA_COMMON
is set to point to the location of pyo-bela/common folder.

    export PYO_BELA_COMMON=/path/to/pyo-bela/common
    ./build_pyo.sh ../../pyo-bela/examples/music-box.py

Documentation
=============

For a complete description of functions that can be used to communicate 
with the pyo embedded processes, see documentation comments in the file 
common/PyoClass.cpp.

(c) 2018 - belangeo

