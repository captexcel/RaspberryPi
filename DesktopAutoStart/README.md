# AutoStart on Desktop Boot
The two files here are for running python scripts on boot to the Desktop on the Raspberry Pi. 
The files need to be placed into the following directory (create autostart folder if it does not exist):
```
/home/pi/.config/autostart
```

***Note:** Utilizing the following two files will require users to modify the files to be executable. This can be accomplished through the Raspberry Pi Terminal using the command listed below.*
```terminal
chmod +x name_of_python_script.py
```


## autostart.desktop
This is useful for running the `numlock.py` script or any script that does not require any action by the user.

## autostart_terminal.desktop
This is useful for running scripts that you may need to see what is going on and for debugging purposes.
