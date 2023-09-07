#/usr/bin/env python

# Importing Modules
import os
import sys

DeviceSpace = int(sys.argv[1])
MinimalDisk = 100

def BigDisk():
    print("Yay You have enough space")
def SmallDisk():
    print("ERROR: You do not have enough disk space to install anything.")
def SameDisk():
    print("WARNING: The install may not install all the way!")

if DeviceSpace > MinimalDisk:
    BigDisk()
elif DeviceSpace < MinimalDisk:
    SmallDisk()
elif DeviceSpace == MinimalDisk:
    SmallDisk()
    