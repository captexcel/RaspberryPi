#!/usr/bin/env python3
# Author: CaptExcel
import os
import time
from gtts import gTTS

speak_greeting = 'Good day!'
file_path = '/home/pi/ECPI/autostart/sounds'
sound_name = '/startup.mp3'

if not os.path.exists(file_path):
    os.makedirs(file_path)
if not os.path.exists(file_path+sound_name):
    greeting_boot = gTTS(speak_greeting)
    greeting_boot.save(file_path+sound_name)

print(speak_greeting)
time.sleep(5)
os.system('mpg321 '+file_path+sound_name+' &') 
