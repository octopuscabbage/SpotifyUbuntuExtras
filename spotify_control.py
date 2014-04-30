import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("-p",action="store_true",dest="playpause",default=False)
parser.add_argument("-n",action="store_true",dest="next",default=False)
parser.add_argument("-l",action="store_true",dest="previous",default=False)

results = parser.parse_args()

if(results.playpause):
	os.popen("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")
if(results.next):
	os.popen("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")
if(results.previous):
	os.popen("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")
