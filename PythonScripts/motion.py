#!/usr/bin/env python3
# ECPI Motion - Raspberry Pi Motion Sensor w/ email
# Author: CaptExcel
'''
Requirements: 
pip3 install gTTS
pip3 install gpiozero
sudo apt-get install mpg321
'''
import os
import time
from gtts import gTTS
from gpiozero import MotionSensor
from email import email_alert

#Define the variables from the user
#gTTS elements
speak_greeting = 'Warning! Warning! Motion has been detected!' #Change this to what you want it to say
speak_entry_sound01 = 'Starting up! Beep Beep Beep Beep Beep! Checking Status.'
speak_entry_sound02 = 'System is Armed and Ready!'
pir = MotionSensor(26) #Set the GPIO read pin to pin 26 to determine if motion is detected
time_check = time.time() #Get the current time
time_last_active = time_check #Set the time_last_active equal to time_check to make the system active
time_last_email = time_check #Set the time_last_email equal to time_check to make the email alert system active
time_delay = 10 #Number of seconds of delay between audible alerts

#Set email variables
time_email_delay = 60 #Number of seconds of delay between email alerts
email_subject = 'Motion Detected!'
email_body = 'Motion has been detected at the office. Please see the attached image for your records.'
email_to = 'YOUR-EMAIL-OR-PHONE-NUMBER'

#Paths to files
sounds_path = '/home/pi/ECPI/Motion/sounds'
pictures_path = '/home/pi/ECPI/Motion/pictures'
logs_path = '/home/pi/ECPI/Motion/logs'
greeting = '/greeting.mp3'
entry_sound01 = '/entry_sound01.mp3'
entry_sound02 = '/entry_sound02.mp3'
logs_file = '/logs.txt'

#check to see if directories for ECPI Motion exist
if not os.path.exists(sounds_path): #check to see if the sounds_path exists
    os.makedirs(sounds_path)
if not os.path.exists(pictures_path): #check to see if the pictures_path exists
    os.makedirs(pictures_path)
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
if not os.path.exists(sounds_path+entry_sound02):
    boot02 = gTTS(speak_entry_sound02)
    boot02.save(sounds_path+entry_sound02)
if not os.path.exists(sounds_path+greeting):
    tts = gTTS(speak_greeting)
    tts.save(sounds_path+greeting)


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
            os.system('cd '+pictures_path)
            os.system('fswebcam -r 1080x1080 --line-colour "#80000000" --banner-colour "#CC000000" --no-shadow --title "ECPIMotion" --subtitle "Python script provided by ECPIgit" --timestamp "%a, %b %d, %Y   |   %I:%M:%S %p %Z" --info "Motion was dedected!" '+pictures_path+'/image.jpg &')
            time.sleep(2)
            os.system('gpicview '+pictures_path+'/image.jpg &')
            time.sleep(10)
            os.system('pkill gpicview')
            os.system('clear')
            motion_time = time.strftime('%a, %b %d, %Y   |   %I:%M:%S %p %Z', time.localtime())
            if time_check >= time_last_email + time_email_delay:
                print('Email message sent:'+str(time.strftime("%I:%M:%S %p",time.localtime(time.time()))))
                logs_open = open(logs_path+logs_file,"at")
                logs_open.write('\nEmail message sent:'+str(time.strftime("%I:%M:%S %p",time.localtime(time.time()))))
                logs_open.close()
                email_alert(email_subject, email_body+'\n\nMotion detected at the office on '+motion_time, email_to, pictures_path+"/image.jpg")
                time_last_email = time.time() + time_email_delay
            else:
                print('Email message not sent:' +str(time.strftime("%I:%M:%S %p",time.localtime(time_last_email+time_email_delay))))
                logs_open = open(logs_path+logs_file,"at")
                logs_open.write('\nEmail message not sent:' +str(time.strftime("%I:%M:%S %p",time.localtime(time_last_email+time_email_delay))))
                logs_open.close()
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
