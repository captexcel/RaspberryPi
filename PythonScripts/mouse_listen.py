#!/usr/bin/env python3
# Mouse Listener
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
from pynput import mouse

# required variables

# main functions
def on_move(x, y):
	print('Pointer moved to {0}'.format((x, y)))
def on_click(x, y, button, pressed):
	print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
	if not pressed:
		#Stop listener
		return False
def on_scroll(x, y, dx, dy):
	print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

# end of file check to see if this file is being opened directly or is being called from another script
if __name__ == ‘__main__’:
	while True:
		with mouse.Listener(
				on_move=on_move,
				on_click=on_click,
				on_scroll=on_scroll) as listener:
			listener.join()
