#/usr/bin/env python

# Importing Modules
import json
import sys
import os

# Vars
InstallJSON = "Install.json"
DeviceSpace = int(sys.argv[1])
MinimalDisk = 100

def BigDisk():
    print("Yay You have enough space")
def SameDisk():
    print("WARNING: The install may not install all the way!")
def SmallDisk():
    print("ERROR: You do not have enough disk space to install anything.")

if DeviceSpace > MinimalDisk:
    BigDisk()
elif DeviceSpace == MinimalDisk:
    SameDisk()
elif DeviceSpace < MinimalDisk:
    SmallDisk()
    