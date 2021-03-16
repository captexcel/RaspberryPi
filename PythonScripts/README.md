# Python Scripts
This collection of python scripts will allow you to do a number of different actions on the Raspberry Pi.

## email.py
This is a basic email handler for sending email through GMail. 
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

## keyboard.py

## motion.py

## motion_front.py

## numlock.py

## rfid.py

## sd_duplicator.py

## startup_sounds.py
