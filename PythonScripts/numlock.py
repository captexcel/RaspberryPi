  
#!/usr/bin/env python3
# Description: Script to automatically turn the num lock on when Raspberry Pi boot
# By default the numlock on the keyboard is set to off if using the Raspberry Pi OS Desktop as of 3/16/2021
# Author: CaptExcel
# Initial Source: 
# Additional Source(s) as used:
'''
# Requirements:
- pip3 install pynput
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
from pynput.keyboard import Key, Controller

# required variables
keyboard = Controller()

# main functions
def numlock():
  print(keyboard.press(Key.num_lock))
  print(keyboard.release(Key.num_lock))

# end of file check to see if this file is being opened directly or is being called from another script
if __name__ == ‘__main__’:
  numlock()
