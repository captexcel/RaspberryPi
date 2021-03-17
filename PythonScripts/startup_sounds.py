#!/usr/bin/env python3
# Description: Create a sounds file to play on boot
# Author: CaptExcel
# Initial Source: 
# Additional Source(s) as used:
'''
# Requirements:
- pip3 install gTTS
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
import time
from gtts import gTTS

# required variables
speak_greeting = 'Good day!'
file_path = '/home/pi/ECPI/autostart/sounds'
sound_name = '/startup.mp3'

# main functions
def startup_sounds():
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    if not os.path.exists(file_path+sound_name):
        greeting_boot = gTTS(speak_greeting)
        greeting_boot.save(file_path+sound_name)

    print(speak_greeting)
    time.sleep(5)
    os.system('mpg321 '+file_path+sound_name+' &') 
# end of file check to see if this file is being opened directly or is being called from another script
if __name__ == ‘__main__’:
    startup_sounds()
