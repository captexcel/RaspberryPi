#!/usr/bin/env python3
# Description: Keyboard HotKey
# Author: CaptExcel
# Initial Source: https://pypi.org/project/pynput/
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
from pynput import keyboard

# required variables

# main functions
def function_1():
    print('Function 1 activated')

def function_2():
    print('Function 2 activated')

def function_3():
    print('Function 3 activated')

    
# end of file check to see if this file is being opened directly or is being called from another script
if __name__ == ‘__main__’:
    print('''
    Press one of the following key combinations:\n
    Function Number 1: [alt]+[ctrl]+r
    Function Number 2: [alt]+[ctrl]+t
    Function Number 3: [alt]+[ctrl]+y
    ''')
    with keyboard.GlobalHotKeys({
            '<alt>+<ctrl>+r': function_1,
            '<alt>+<ctrl>+t': function_2,
            '<alt>+<ctrl>+y': function_3}) as h:
        h.join()
