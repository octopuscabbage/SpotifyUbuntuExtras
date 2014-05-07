#!/usr/bin/env python

import dbus
import subprocess
import time
import inspect, os
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-d",action="store_true",dest="display",default=False) #can be used to display a new notification


global python_version
if sys.version_info[0] == 3:
    python_version = 3
elif sys.version_info[0] == 2:
    python_version = 2
else:
    python_version = 1
        
results = parser.parse_args()


update_time  = 3 # The time to wait between checks (in seconds)
expire_time  = 4000 # The expiration time of the notifications (in milliseconds)
logo_abspath = 'spotify_80.png' # The path to a logo that will be displayed in the notification, this is not in the github repo due to copyright concerns


# logo_abspath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/' + logo_abspath
thumb_path    = '/tmp/spotify_notification_thumb'
wget_log_path = '/tmp/spotify_notification_wget.log'

global current_track
current_track = ""

global current_thumb
current_thumb = ""

def extract_str(dbus_str):
    return dbus_str.encode('utf-8')

def update():
    global current_thumb
    bus = dbus.SessionBus()
    player = bus.get_object('com.spotify.qt', '/')
    iface = dbus.Interface(player, 'org.freedesktop.MediaPlayer2')
    info = iface.GetMetadata()

    try:
        thumb_url = str(info['mpris:artUrl'])
        if current_thumb != thumb_url:
            current_thumb = thumb_url
            subprocess.call(['wget', '-O', thumb_path, '-o', wget_log_path, thumb_url])
        if python_version==2:
            return "Title: \t\t" + extract_str(info['xesam:title'])+"\nArtist: \t\t" + extract_str(info['xesam:artist'][0]) + "\nAlbum: \t" + extract_str(info['xesam:album'])
        elif python_version==3:
            return "Title: \t\t" + str(info['xesam:title'])+"\nArtist: \t\t" + str(info['xesam:artist'][0]) + "\nAlbum: \t" + str(info['xesam:album'])

    except KeyError: #Sometimes songs in other languages screw up
        return ""

def notify():
    global current_track
    track_now = update()
    if track_now != current_track:
        current_track = track_now
        subprocess.call(['notify-send', '--expire-time=' + str(expire_time), '--icon=' + thumb_path, track_now])

if __name__ == '__main__' :
    if(results.display): #display a notification on demand
        notify()
    else:
        while True:
            notify()
            time.sleep(update_time)
