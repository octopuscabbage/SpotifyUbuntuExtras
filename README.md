#Spotify Extras for Ubuntu Linux

#Spotify Extras for Ubuntu Linus

These scripts were designed to add some extra functionality to Spotify on Ubuntu. 

All scripts use dbus and no external libraries (that are not built into python) Tested on python 3.4, though they should work on 2.x probably.

##spotify_control.py: An easier command line utility for controlling spotify through dbus

###Usage:

```
'$ spotify_control.py -n' => go to next song
'$ spotify_control.py -p' => play/pause the current song
'$ spotify_control.py -l' => go to previous song
```

##spotify_notifications.py: Desktop notifications for spotify through python

###Usage:
	Just run the script and the notifications will appear. Tweak update time to your liking.
