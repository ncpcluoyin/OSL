#!/usr/bin/python3
import os
print("Uninstalling")
os.system("rm -rf /opt/osl/")
os.system("apt autoremove arch-install-scripts -y")
print("OK")
