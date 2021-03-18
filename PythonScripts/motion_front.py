#!/usr/bin/env python3
# Title: ECPI Motion (Front Door)
# Description: Raspberry Pi Motion Sensor to play audio file created using Google text-to-speech
# Author: CaptExcel
# Initial Source: 
# Additional Source(s) as used:
'''
# Requirements: 
- pip3 install gTTS
- pip3 install gpiozero
- sudo apt-get install mpg321
'''
'''
# Needed Supplies:
- (1) PIR Motion Sensor
- (3) Female-to-Male Jumper Wires
'''
'''
# Reference Material:
- PIR Motion Sensor Pinout to the Raspberry Pi 4 GPIO headers (PIN Number Reference: https://www.raspberrypi.org/documentation/usage/gpio/)
5v.    -->  PIN 2
Signal -->  PIN 37 (GPIO 26)
Ground -->  PIN 39
'''

# import required libraries
import os
import time
from gtts import gTTS
from gpiozero import MotionSensor

# define global variables
'''
# TO RECORD NEW MESSAGES:
# GO TO /home/pi/ECPI/sounds
# DELETE entry_sound01.mp3
# DELETE entry_sound02.mp3
# DELETE greeting.mp3
'''
#Define the variables from the user
#gTTS elements
speak_greeting = 'Welcome to ECPI University! Please remember to follow COVID protocols.' #Change this to what you want it to say
speak_entry_sound01 = 'Starting up! Getting ready to change lives. Checking Status.'
speak_entry_sound02 = 'System is Ready!'
pir = MotionSensor(26) #Set the GPIO read pin to pin 26 to determine if motion is detected
time_delay = 10 #Number of seconds of delay between audible alerts

##################################
### DO NOT EDIT BELOW THIS LINE###
##################################
time_check = time.time() #Get the current time
time_last_active = time_check #Set the time_last_active equal to time_check to make the system active
#Paths to files
sounds_path = '/home/pi/ECPI/sounds'
logs_path = '/home/pi/ECPI/logs'
greeting = '/greeting.mp3'
entry_sound01 = '/entry_sound01.mp3'
entry_sound02 = '/entry_sound02.mp3'
logs_file = '/logs.txt'

# main functions
def motion_front():
    #check to see if directories for ECPISecure exist
    if not os.path.exists(sounds_path): #check to see if the sounds_path exists
        os.makedirs(sounds_path)
    if not os.path.exists(logs_path): #check to see if the logs_path exists
        os.makedirs(logs_path)
    if not os.path.exists(logs_path+logs_file): #check to see if the logs_path exists
        os.mknod(logs_path+logs_file)

    logs_open = open(logs_path+logs_file,"at")
    logs_open.write('\nDate: '+ str(time.strftime("%I:%M:%S %p",time.localtime(time.time())))+' ')
    logs_open.close()

    #Create gTTS sounds if files do not already exist
    #This will cut down on the gTTS requests sent
    if not os.path.exists(sounds_path+entry_sound01):
        boot01 = gTTS(speak_entry_sound01)
        boot01.save(sounds_path+entry_sound01)
        time.sleep(2)
    if not os.path.exists(sounds_path+entry_sound02):
        boot02 = gTTS(speak_entry_sound02)
        boot02.save(sounds_path+entry_sound02)
        time.sleep(2)
    if not os.path.exists(sounds_path+greeting):
        tts = gTTS(speak_greeting)
        tts.save(sounds_path+greeting)
        time.sleep(2)

    time.sleep(1)
    #Play Start-up sounds
    os.system('mpg321 '+sounds_path+entry_sound01) #play entry_sound01 on startup

    while True:
        time_check = time.time()
        if time_check >= time_last_active + time_delay:
            print('\n\n' + speak_entry_sound02 +' '+str(time.strftime("%I:%M:%S %p",time.localtime(time.time()))) + '\n\n')
            os.system('mpg321 '+sounds_path+entry_sound02)
            pir.wait_for_motion()
            while pir.value==1:
                print('\n\n' + str(pir.value) + ': ' + speak_greeting + ' ' + str(time.strftime("%I:%M:%S %p",time.localtime(time.time()))) + '\n\n')
                os.system('mpg321 '+sounds_path+greeting+' &')
                time.sleep(10)
                motion_time = time.strftime('%a, %b %d, %Y   |   %I:%M:%S %p %Z', time.localtime())
                pir.wait_for_no_motion()
                time_last_active = time.time() + time_delay
        else:
            if pir.value == 0:
                print(str(pir.value)+': System Arming. No Motion Detected. System active again at:' +str(time.strftime("%I:%M:%S %p",time.localtime(time_last_active+time_delay))))
                logs_open = open(logs_path+logs_file,"at")
                logs_open.write('\n'+str(pir.value)+': System Arming. No Motion Detected. System active again at:' +str(time.strftime("%I:%M:%S %p",time.localtime(time_last_active+time_delay))))
                logs_open.close()
            else:
                print(str(pir.value)+': System Arming. Motion Detected. System active again at:' +str(time.strftime("%I:%M:%S %p",time.localtime(time_last_active+time_delay))))
                logs_open = open(logs_path+logs_file,"at")
                logs_open.write('\n'+str(pir.value)+': System Arming. Motion Detected. System active again at:' +str(time.strftime("%I:%M:%S %p",time.localtime(time_last_active+time_delay))))
                logs_open.close()
        time.sleep(1)

# end of file check to see if this file is being opened directly or is being called from another script
if __name__ == ‘__main__’:
    motion_front()
