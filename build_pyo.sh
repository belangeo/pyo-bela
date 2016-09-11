#!/bin/bash
#
# This script compiles a pyo project on the BeagleBone Black and runs it. 
# Pass the python file to run in the first argument. The project name will
# be the name of the file (without ".py").
# Pass the path to the "pyo-bela/common" folder in the second argument to 
# include all needed files to run the project. The second argument can be 
# ommited if an environment variable called PYO_BELA_COMMON is set to 
# point to the "pyo-bela/common" folder.

mainfile="$1"
basename="${mainfile##*/}"
project="${basename%.*}"

if [ -n "$PYO_BELA_COMMON" ]; then
    common="$PYO_BELA_COMMON";
else
    common="$2";
fi

mkdir ${project}
cp ${mainfile} ${project}/main.py
cp ${common%/}/* ${project}/

./build_project.sh ${project} -f -m 'CPPFLAGS="-I/usr/include/python2.7 -I/usr/include/arm-linux-gnueabihf/python2.7 -fno-strict-aliasing -D_FORTIFY_SOURCE=2 -g0 -fstack-protector-strong -Wformat -Werror=format-security -DNDEBUG -fwrapv -Wall -Wstrict-prototypes -O3 -march=armv7-a -mtune=cortex-a8 -mfloat-abi=hard -mfpu=neon -ftree-vectorize" LDFLAGS="-L/usr/lib/python2.7/config-arm-linux-gnueabihf -L/usr/lib" LDLIBS="-lpython2.7 -lpthread -ldl -lutil -lm -Xlinker -export-dynamic -Wl,-O3 -Wl,-Bsymbolic-functions"'

rm -r ${project}

