#!/bin/sh
udevd --daemon
udevadm trigger

echo "starting python script"
python /usr/src/app/stockPrice.py