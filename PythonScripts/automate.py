#!/usr/bin/env python3
# Title: Robotic Process Automation (RPA)
# Description: Automation for sending and email
# Use the Raspberry Pi to automate a specified action
# Author: CaptExcel
# Initial Source: https://pyautogui.readthedocs.io/en/latest/
'''
# Requirements:
- pip3 install pyautogui
'''
'''
# Needed Supplies:
- N/A
'''
'''
# Refrence Material:
- Mouse
.moveTo(x,y,duration=num_seconds)
.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
.rightClick(x=moveToX, y=moveToY)
.middleClick(x=moveToX, y=moveToY)
.doubleClick(x=moveToX, y=moveToY)
.tripleClick(x=moveToX, y=moveToY)
.scroll(amount_to_scroll, x=moveToX, y=moveToY)

- Keyboard
.typewrite('Hello world!\n', interval=secs_between_keys)  # useful for entering text, newline is Enter
.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)
.press('enter')
.hotkey('ctrl', 'c')  # ctrl-c to copy
.hotkey('ctrl', 'v')  # ctrl-v to paste
.keyDown(key_name)
.keyUp(key_name)

- Images
.locateCenterOnScreen('looksLikeThis.png')  # returns center x and y
'''

# import required libraries
import pyautogui
from time import sleep, localtime, strftime

# define global variables
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True

move_duration = .3
type_speed = .07
my_confidence = 0.7

# main functions
def send_email_from_outlook():
    pyautogui.click(pyautogui.locateCenterOnScreen('/home/pi/ECPI/images/chromium.png'), duration=move_duration)
    sleep(5)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('t')
    sleep(.1)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('t')
    sleep(.9)
    pyautogui.typewrite('https://outlook.live.com/owa/?nlp=1',interval=type_speed)
    pyautogui.press('enter')
    sleep(.9)
    pyautogui.press('f11')
    sleep(5)
    pyautogui.typewrite('YOUR-OUTLOOK.COM-EMAIL-ADDRESS',interval=type_speed)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.typewrite('YOUR-PASSWORD',interval=type_speed)
    pyautogui.press('enter')
    sleep(10)
    not_loaded = pyautogui.locateOnScreen('/home/pi/ECPI/images/outlook_wait.png')
    while not_loaded:
        sleep(.01)
        pyautogui.moveTo(800,800,duration=move_duration)
        pyautogui.moveTo(300,800,duration=move_duration)
        pyautogui.moveTo(800,800,duration=move_duration)
        not_loaded = pyautogui.locateOnScreen('/home/pi/ECPI/images/outlook_wait.png')
    pyautogui.click(pyautogui.locateCenterOnScreen('/home/pi/ECPI/images/outlook_new_message.png'), duration=move_duration)
    sleep(15)
    pyautogui.typewrite('captexcel@outlook.com',interval=type_speed)
    pyautogui.press('tab')
    sleep(.1)
    pyautogui.press('tab')
    sleep(.1)
    pyautogui.press('tab')
    sleep(.1)
    pyautogui.typewrite('John Doe Imposter Arrived at:'+strftime('%a, %b %d, %Y   |   %r', localtime()),interval=type_speed)
    pyautogui.press('tab')
    pyautogui.typewrite('Someone by the name of John Doe who was an imposter tried to enter the building today('+strftime('%a, %b %d, %Y   |   %r).\n\nThankfully, access was not granted, and we have the attached photo as evidence.\n\nSincerely,\nMr. Ayers, aka CaptExcel', localtime()),interval=type_speed)
    sleep(3)
    ### Load image that was taken
    pyautogui.click(pyautogui.locateCenterOnScreen('/home/pi/ECPI/images/outlook_new_msg_attach.png'), duration=move_duration)
    sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('/home/pi/ECPI/images/outlook_new_msg_attach_two.png'), duration=move_duration)
    sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('/home/pi/ECPI/images/outlook_image_filepath.png'), duration=move_duration)
    sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('/home/pi/ECPI/images/outlook_attachment.png'), duration=move_duration)
    sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('/home/pi/ECPI/images/save_open.png'), duration=move_duration)
    sleep(5)
    pyautogui.click(pyautogui.locateCenterOnScreen('/home/pi/ECPI/images/outlook_send_message.png'), duration=move_duration)
    sleep(5)
    pyautogui.click(pyautogui.locateCenterOnScreen('/home/pi/ECPI/images/outlook_user.png'), duration=move_duration)
    sleep(5)
    pyautogui.moveTo(800,800,duration=move_duration)
    pyautogui.click(pyautogui.locateCenterOnScreen('/home/pi/ECPI/images/outlook_sign-out.png'), duration=move_duration)
    sleep(5)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('F4')
    sleep(.1)
    pyautogui.keyUp('alt')
    pyautogui.keyUp('F4')

# end of file check to see if this file is being opened directly or is being called from another script
if __name__ == '__main__':
    send_email_from_outlook()
