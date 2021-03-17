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

<br/></br>
## 🐍 email.py
>Description: This is a basic email handler for sending email through GMail. 
### Dependencies required:
```

```
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

<br/></br>
## 🐍 motion.py
>Description: 

<br/></br>
## 🐍 motion_front.py
>Description: 

<br/></br>
## 🐍 mouse_listen.py
>Description: This script will print out the location of the mouse cursor when moved. This can be helpful when utilizing the **pynput** library to get the specific cooridantes of the mouse cursor.

<br/></br>
## 🐍 numlock.py
>Description: This utilizes the **pynput** library to turn on the numlock. By default the Raspberry Pi has the numlock off.

<br/></br>
## 🐍 rfid.py
>Description: 

<br/></br>
## 🐍 sd_duplicator.py
>Description: This will create an image from a *master* image file, reduce the size of the image (to speed up the next process), and then duplicate a specified number  of SD cards for the Raspberry Pi.  

<br/></br>
## 🐍 startup_sounds.py
>Description: This uses the Google text-to-speech (**gTTS**) library to create a startup message that can be autoplayed at startup of your Raspberry Pi.
