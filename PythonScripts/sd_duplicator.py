#!/usr/bin/env python3
# Title: SD Card Duplicator 
# Description: Duplicate more than one SD Card at a time using the Raspberry Pi and a USB 3.0 Hub
# Author: CaptExcel
# Initial Source: https://ccse.kennesaw.edu/outreach/raspberrypi/duplicate_sd.php
# Additional Source(s) as used:
'''
# Requirements:
- pip3 install gTTS
'''
'''
# Needed Supplies:
- (1) USB 3.0 4 port hub
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
file_path = '/duplicator'
dependencies = 'Installing dependencies now.'
dependencies_sound = '/dependencies.mp3'
img_created = 'Image has been created.'
img_created_sound = '/image.mp3'
img_duplicated = 'Duplication has been completed.'
img_duplicated_sound = '/duplicated.mp3'

yes = set(['yes','y','Y','YES'])
no = set(['no','n','N','NO'])

# main functions
if not os.path.exists(file_path):
    os.makedirs(file_path)
if not os.path.exists(file_path+img_created_sound):
    greetingboot = gTTS(img_created)
    greetingboot.save(file_path+img_created_sound)
if not os.path.exists(file_path+img_duplicated_sound):
    greetingboot = gTTS(img_duplicated)
    greetingboot.save(file_path+img_duplicated_sound)

def install_dependencies():
    while True:
        choice = input('Would you like to install the dependencies?: [y/n]').lower()
        if choice in yes:
            print(dependencies+' Please wait...')
            os.system('mpg321 '+file_path+dependencies_sound+' &')
            os.system('sudo apt-get install dcfldd')
            os.system('wget https://raw.githubusercontent.com/Drewsif/PiShrink/master/pishrink.sh')
            os.system('chmod +x pishrink.sh')
            os.system('sudo mv pishrink.sh /usr/local/bin')
        elif choice in no:
            print('Moving on')
            return False
        else:
            print("Please respond with 'yes' or 'no'\n")
def create_image():
    img_name = img_name
    while True:
        choice = input('Would you like create a new image?: [y/n]  ').lower()
        if choice in yes:
            named_tuple = time.localtime() # get struct_time
            time_string = time.strftime("%Y-%m-%d", named_tuple)
            new_img_name = 'ecpi-'+time_string+'.img'
            print(img_created+' Please wait...')
            os.system('mpg321 '+file_path+img_created_sound+' &')
            os.system('sudo umount /dev/sd*')
            os.system('sudo dd bs=4096 if=/dev/sda of='+new_img_name)
            os.system('sudo sync')
            os.system('sudo pishrink.sh '+new_img_name) #Shrink the image
            make_duplicates(new_img_name)
        elif choice in no:
            old_img_name = input('What is the name of the image you want to use?: ')
            make_duplicates(old_img_name)
            return False
        else:
            print("Please respond with 'yes' or 'no'\n")
def make_duplicates(my_img_name):
    img_name = my_img_name
    while True:
        choice = input('Would you like to make duplicates?: [y/n] ').lower()
        if choice in yes:
            num_copies = input('How many copies?: [1-4] ')
            print(img_duplicated+' Please wait...')
            os.system('mpg321 '+file_path+img_duplicated_sound+' &')
            #Make copies
            if num_copies == '1':
                os.system('sudo dcfldd bs=64k if='+img_name+' of=/dev/sda')
            elif num_copies == '2':
                os.system('sudo dcfldd bs=64k if='+img_name+' of=/dev/sda of=/dev/sdb')
            elif num_copies == '3':
                os.system('sudo dcfldd bs=64k if='+img_name+' of=/dev/sda of=/dev/sdb of=/dev/sdc')
            elif num_copies == '4':
                os.system('sudo dcfldd bs=64k if='+img_name+' of=/dev/sda of=/dev/sdb of=/dev/sdc of=/dev/sdd')
            else:
                print("Please respond with a quantity between '1' and '4'\n")
        elif choice in no:
            break
        else:
            print("Please respond with 'yes' or 'no'\n")
# end of file check to see if this file is being opened directly or is being called from another script
if __name__ == "__main__":
    input('Press Enter to continue...')
    install_dependencies()
    create_image()
