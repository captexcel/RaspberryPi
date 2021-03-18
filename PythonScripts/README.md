# Python Scripts
This collection of python scripts will allow you to do a number of different actions on the Raspberry Pi.

### General Information for Raspberry Pi
In order to execute the python script you may need to grant permissions to run it from the Raspberry Pi Terminal. This is required when running the file automatically on the Desktop boot option explained in the [`./DesktopAutoStart`](https://github.com/captexcel/RaspberryPi/tree/main/DesktopAutoStart) Folder
```terminal
chmod +x name_of_python_script.py
```

<br/></br>
# Python Script Descriptions
## 🐍 automate.py
>Description: This is a very basic Robtic Process Automation (RPA) script utilizing the **pyautogui** library.
#### Requirements:
```
pip3 install pyautogui
```
#### Suppplies Needed:
- N/A
#### Refrence Material:
- Mouse
  - .moveTo(x,y,duration=num_seconds)
  - .click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
  - .rightClick(x=moveToX, y=moveToY)
  - .middleClick(x=moveToX, y=moveToY)
  - .doubleClick(x=moveToX, y=moveToY)
  - .tripleClick(x=moveToX, y=moveToY)
  - .scroll(amount_to_scroll, x=moveToX, y=moveToY)
- Keyboard
  - .typewrite('Hello world!\n', interval=secs_between_keys)  # useful for entering text, newline is Enter
  - .typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)
  - .press('enter')
  - .hotkey('ctrl', 'c')  # ctrl-c to copy
  - .hotkey('ctrl', 'v')  # ctrl-v to paste
  - .keyDown(key_name)
  - .keyUp(key_name)
- Images
  - .locateCenterOnScreen('looksLikeThis.png')  # returns center x and y

<br/></br>
## 🐍 base.py
>Description: Template for future python scripts.

<br/></br>
## 🐍 email.py
>Description: This is a basic email handler for sending email through GMail. 
#### Requirements:
- N/A
#### Suppplies Needed:
- N/A
#### Refrence Material:
You will need to set up 2FA and get a code from the GMail settings. You can then update the following two lines of code:
```python
user = "YOUR-GMAIL-ACCOUNT"
password = "YOUR-GOOGLE-2FA-AUTH-CODE" #Comment out to debug
```
**Note:** Commenting out the `password` line will and uncommenting out the `password` line further into the script will allow for debuging.

This can be called from another script by passing in the `subject` of the email, the `body` of the email, the email address of who it is going `to`, and the local image path (`ipath`) to the image to attach.

<br/></br>
## 🐍 keyboard.py
>Description: This utilizes the **pynput** library to create hotkeys for different functions.
#### Requirements:
```
pip3 install pynput
```
#### Suppplies Needed:
- N/A
#### Refrence Material:
- N/A

<br/></br>
## 🐍 motion.py
>Description: Raspberry Pi Motion Sensor w/ email
#### Requirements:
```
pip3 install gTTS
pip3 install gpiozero
sudo apt-get install mpg321
```
#### Suppplies Needed:
- (1) PIR Motion Sensor
- (3) Female-to-Male Jumper Wires
#### Refrence Material:
- PIR Motion Sensor Pinout to the Raspberry Pi 4 GPIO headers (PIN Number Reference: https://www.raspberrypi.org/documentation/usage/gpio/)
  - 5v.    -->  PIN 2
  - Signal -->  PIN 37 (GPIO 26)
  - Ground -->  PIN 39

<br/></br>
## 🐍 motion_front.py
>Description: Raspberry Pi Motion Sensor w/ email
#### Requirements:
```
pip3 install gTTS
pip3 install gpiozero
sudo apt-get install mpg321
```
#### Suppplies Needed:
- (1) PIR Motion Sensor
- (3) Female-to-Male Jumper Wires
#### Refrence Material:
- PIR Motion Sensor Pinout to the Raspberry Pi 4 GPIO headers (PIN Number Reference: https://www.raspberrypi.org/documentation/usage/gpio/)
  - 5v.    -->  PIN 2
  - Signal -->  PIN 37 (GPIO 26)
  - Ground -->  PIN 39


<br/></br>
## 🐍 mouse_listen.py
>Description: This script will print out the location of the mouse cursor when moved. This can be helpful when utilizing the **pynput** library to get the specific cooridantes of the mouse cursor.
#### Requirements:
```
pip3 install pynput
```
#### Needed Supplies:
- N/A
#### Reference Material:
- N/A

<br/></br>
## 🐍 numlock.py
>Description: This utilizes the **pynput** library to turn on the numlock. By default the Raspberry Pi has the numlock off.
#### Requirements:
```
pip3 install pynput
```
#### Needed Supplies:
- N/A
#### Reference Material:
- N/A


<br/></br>
## 🐍 rfid.py
>Description: Read and write RFID chips/badges using the RFID-RC522 board
#### Requirements: 
```
pip3 install mfrc522
pip3 install gpiozero
```
#### Needed Supplies:
- (1) RFID-RC522 Board
- (7) Header jumper wires
#### Reference Material:
- RFID-RC522 Pinout to the Raspberry Pi 4 GPIO headers
  - SDA  -->  PIN 24
  - SCK  -->  PIN 23
  - MOSI -->  PIN 19
  - MISO -->  PIN 21
  - GND  -->  PIN 6
  - RST  -->  PIN 22
  - 3.3v -->  PIN 1

<br/></br>
## 🐍 sd_duplicator.py
>Description: This will create an image from a *master* image file, reduce the size of the image (to speed up the next process), and then duplicate a specified number  of SD cards for the Raspberry Pi.  
#### Requirements: 
```
pip3 install gTTS
```
#### Needed Supplies:
- (1) USB 3.0 4 port hub
#### Reference Material:
- N/A

<br/></br>
## 🐍 startup_sounds.py
>Description: This uses the Google text-to-speech (**gTTS**) library to create a startup message that can be autoplayed at startup of your Raspberry Pi.
#### Requirements: 
```
pip3 install gTTS
```
#### Needed Supplies:
- N/A
#### Reference Material:
- N/A
