  
#!/usr/bin/env python3
# Script to automatically turn the num lock on when Raspberry Pi boot
# By default the numlock on the keyboard is set to off if using the Raspberry Pi OS Desktop as of 3/16/2021
# Author: CaptExcel
from pynput.keyboard import Key, Controller
keyboard = Controller()
print(keyboard.press(Key.num_lock))
print(keyboard.release(Key.num_lock))
