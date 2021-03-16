#!/usr/bin/env python3
# Keyboard HotKey
# Author: CaptExcel
# Initial Source: https://pypi.org/project/pynput/
'''
Requirements:
pip3 install pynput
'''
from pynput import keyboard

def function_1():
    print('Function 1 activated')

def function_2():
    print('Function 2 activated')

def function_3():
    print('Function 3 activated')

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
