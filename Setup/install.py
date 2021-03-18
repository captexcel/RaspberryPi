#!/usr/bin/env python3
# Description: Install Required Dependencies for the appropriate script
# Author: CaptExcel
# Initial Source:
# Additional Source(s) as used:
'''
# Requirements:
- N/A
'''
'''
# Needed Supplies:
- N/A
'''
'''
# Reference Material:
- N/A
'''

# import required libraries
import os
import sys

# required global variables
comment = (["#"])
args = (["-f","-h"])

# main functions
def install_requirements():
    f = open('./requirements.txt', 'r')
    #print("Install File: requirements.txt")
    for x in f:
        if x[:1].replace("\n","") not in str(comment[:1]):
            os.system(x)
            print(x.strip()+' Install Completed')

def install_file(a_v):
    f = open(a_v, 'r')
    #print("Install File: "+a_v)
    for x in f:
        if x[:1].replace("\n","") not in str(comment[:1]):
            os.system(x)
            print(x.strip()+' Install Completed')

def install(a_v):
    if str(a_v[1]) not in args:
        install_requirements()
    elif str(a_v[1]) == "-h":
        print('''
        Usage from terminal:

        1. Install a custom files list
        python3 install.py -r your-file-name
        
        2. Install the requirements.txt file
        python3 install.py

        Written by CaptExcel''')
    else:
        for x in a_v[2:]:
            install_file(x)

# end of file check to see if this file is being opened directly or is being called from another script
if __name__ == '__main__':
    install(sys.argv)
