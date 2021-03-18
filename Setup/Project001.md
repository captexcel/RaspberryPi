## Project #1: Configuration of Raspberry Pi into Network Attached Storage (NAS) Device
###### Latest Update: 03/10/2021
#### Step 1: Setup and prepare the file location
Open Terminal on your Raspberry Pi and type the following commands and hit enter after each line.
```terminal
sudo mkdir -p /home/pi/ECPI/Storage/share
```
```terminal
sudo chmod –R 777 /home/pi/ECPI/Storage/share
```
#### Step 2: Get Ready to Samba
What is Samba? “Samba is the standard Windows interoperability suite of programs for Linux and Unix” (Samba.org, 2020). This will allow you to connect to your Raspberry Pi from another computer (Windows or Mac).
```terminal
sudo nano /etc/samba/smb.conf
```
Tell Samba where the shared folder we created in Step 1 is located. Use the arrow keys to move to the bottom of the file and enter the following just as it is written:
```terminal
[ECPIstorage]
path = /home/pi/ECPI/Storage/share
writeable = yes
create mask = 0777
directory mask = 0777
public = no
```

Press **`CTRL`**+**`X`**
Press **`Y`**
Press **`ENTER`**

#### Step 3: Restart the Samba service
```terminal
sudo systemctl restart smbd
```
#### Step 4: Set a password you will remember
We need to set a password to protect your new shared folder location…and also your new dance moves (the samba).
```terminal
sudo smbpasswd –a pi
```
Password: _______________________
<br/></br>
#### Step 5: Reboot your Raspberry Pi
Reboot the Raspberry Pi by typing the following command into terminal and hitting enter.
```terminal
sudo reboot
```
#### Step 6: Celebrate!

## Accessing the files from your home computer
Plug in and connect your Raspberry Pi to your Wifi network.

### Windows
On a Windows computer open `File Explorer` > `This PC` > `Computer` (tab at the top) > `Map Network Drive`
Enter the following for the folder: `\\ecpi\ECPIstorage`
Click on the checkbox that says `Connect using different credentials`
Click `Finish`
You will then be prompted to enter your username **`pi`** and **`password`** 
Click `Finish`

### Mac
IP Address: ____________________

On your Raspberry Pi open Terminal to retrieve your IP Address by typing the following into the terminal and hitting enter.
```terminal
hostname –I
```
On a Mac computer open `Finder` > `Go` > `Connect to Server`
Type the following in when prompted: `smb://192.168.0.15/ECPIstorage`
Note: change `192.168.0.15` to your IP Address from the `hostname -I` command

<br/></br>
<br/></br>
## References:
- Emmet. (2021, February 9). *How to setup a raspberry pi samba server.* https://pimylifeup.com/raspberry-pi-samba/. 
- Gordon, W. (2019, December 30). *How to turn a raspberry pi into a nas for whole-home file sharing.* https://www.pcmag.com/how-to/how-to-turn-a-raspberry-pi-into-a-nas-for-whole-home-file-sharing. 
- Samba.org. (2020). *What is samba? Samba.* https://www.samba.org/samba/what_is_samba.html.
- Zwetsloot, R. (2019). *Build a raspberry pi nas.* https://magpi.raspberrypi.org/articles/build-a-raspberry-pi-nas. 
