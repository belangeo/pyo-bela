mkdir tmp
cd tmp
echo "=== Downloading pyo-bela binaries. ==="
wget -q https://github.com/belangeo/pyo-bela/releases/download/v0.9.0/dist-packages.tar.bz2
echo "=== Extracting pyo-bela binaries. ==="
tar xjf dist-packages.tar.bz2
echo "=== Copying files to the BBB. ==="
scp -r -q dist-packages/ root@192.168.7.2:/usr/local/lib/python2.7/
echo "=== Cleanup. ==="
cd ..
rm -r tmp
echo "=== Done! ==="

