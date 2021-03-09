#!/usr/bin/env python3
import os
import time
from gtts import gTTS

speak_greeting = 'Good day! System is now starting!'
file_path = 'home/pi/.config/autostart/sounds'
sound_name = '/startup.mp3'

if not os.path.exists(file_path):
    os.makedirs(file_path)
if not os.path.exists(file_path+sound_name)
    greetingboot = gTTS(speak_greeting)
    greetingboot.save(file_path+sound_name)

print(speak_greeting)
time.sleep(5)
os.system('mpg321 '+file_path+sound_name+' &')