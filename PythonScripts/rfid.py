#!/usr/bin/env python3
# RFID Reader/Writer for Raspberry Pi 4
# Author: CaptExcel
# Initial Source: https://pimylifeup.com/raspberry-pi-rfid-rc522/
'''
Requirements:
'''
'''
Needed Supplies:
- RFID-RC522 Board
- Header jumper wires
'''
'''
Reference Material:
RFID-RC522 Pinout to the Raspberry Pi 4 GPIO headers
SDA  -->  PIN 24
SCK  -->  PIN 23
MOSI -->  PIN 19
MISO -->  PIN 21
GND  -->  PIN 6
RST  -->  PIN 22
3.3v -->  PIN 1
'''

# import required libraries
#Comment out the next two lines if this is the first time using the Raspberry Pi RFID Reader
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import os
import time

# required variables
yes = (['Y','y','YES','yes'])
no = (['N','n','NO','no'])

# main functions
#Install all dependencies required to run this script
#Note: You will need to comment out the two lines referenced above before running this script or it will result in an error
def install_dependencies():
	print('Enable SPI in the Raspi-config')
	wait = input('Press enter to continue')
	os.system('sudo raspi-config')
	os.system('sudo apt-get install python3-dev python3-pip')
	os.system('sudo pip3 install spidev')
	os.system('sudo pip3 install mfrc522')

#Read to RFID card
def read_rfidcard():
	reader = SimpleMFRC522()
	try:
			id, text = reader.read()
			print(id)
			print(text)
	finally:
			GPIO.cleanup()

#Write to RFID card
def write_rfidcard():
	reader = SimpleMFRC522()
	try:
			text = input('New data:')
			print("Now place your tag to write")
			reader.write(text)
			print("Written")
	finally:
			GPIO.cleanup()
#Decide to write or read card
def make_decision():
	while True:
		choice = input('Write new card? [y/n]: ').lower()
		if choice in yes:
			write_rfidcard()
		elif choice in no:
			read_rfidcard()
		else:
			print('Closing!')
			exit()

# end of file check to see if this file is being opened directly or is being called from another script
if __name__ == ‘__main__’:
	while True:
		choice = input('Install Dependencies? [y/n]: ').lower()
		if choice in yes:
			install_dependencies()
		elif choice in no:
			make_decision()
		else:
			make_decision()
