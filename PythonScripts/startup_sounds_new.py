#!/usr/bin/env python3
# Title: Startup Sounds
# Description: Create a sounds file to play on boot
# Author: CaptExcel
# Initial Source: 
# Additional Source(s) as used:
'''
# Requirements:
- pip3 install gTTS
- sudo apt-get install mpg321
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

# define global variables
speak_greeting = 'Hello, Welcome to the Raspberry Pi Experience brought to you by ECPI University Innsbrook Campus!'
sound_name = '/startup.mp3'

# main functions
greeting_boot = gTTS(speak_greeting)
greeting_boot.save(sound_name)
time.sleep(5)
os.system('mpg321 '+sound_name+' &') 

'''
Directions:
1. Open mu Python3 IDE (Raspberry Pi menu icon->Programming->mu)
2. Write the code above
3. Save the file to the desktop
4. Run the file
5. Open Terminal (Black and Blue menu icon)
6. Enter the following commands and hit enter at the end of each line
    cd .config/autostart
    nano sounds.desktop
    [Desktop Entry]
    Type=Application
    Name=WelcomeSounds
    Exec=/usr/bin/lxterminal -e "sleep 5 && cd /home/pi/Desktop && python3 ./sounds.py && sleep infinity"
    Path=
    Press the following keyboard keys [CTRL]+[s] then [CTRL]+[x]
    reboot
7. Listen for the startup sound once it restarts
'''
