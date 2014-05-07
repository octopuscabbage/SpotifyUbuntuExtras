#Spotify Extras for Ubuntu Linux

These scripts were designed to add some extra functionality to Spotify on Ubuntu. 

From the reddit comments on this thread it should work with the free linux client. I test on the paid version.

All scripts use dbus and no external libraries (that are not built into python) Tested on python 3.4, though they should work on 2.x.

##Tested on:
Xubuntu - 14.04, 13.10
ArchLinux - http://www.reddit.com/r/Ubuntu/comments/24eu6n/control_spotify_easily_from_the_command_line_and/ch6lnby


##spotify_control.py: An easier command line utility for controlling spotify through dbus

This can be used to more easily map Multimedia Keys or other things to song controls. 
(I personally have Super+Q for previous, Super+W for pause, and Super+E for next)

###Usage:

```
$ spotify_control.py -n
```
=> go to next song
```
$ spotify_control.py -p
```
=> play/pause the current song
```
$ spotify_control.py -l 
```

=> go to previous song

##spotify_notifications.py: Desktop notifications for spotify through python

###Usage:
	```
	$spotify_control.py -d
	```
	=> display a new notification


	Just run the script and the notifications will appear. Tweak update time to your liking.
