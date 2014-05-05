import dbus
import subprocess
import time
import inspect, os

update_time  = 3 # The time to wait between checks (in seconds)
expire_time  = 4000 # The expiration time of the notifications (in milliseconds)
logo_abspath = 'spotify_80.png' # The path to a logo that will be displayed in the notification

logo_abspath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/' + logo_abspath

global current_track
current_track = ""

def update():
    bus = dbus.SessionBus()
    player = bus.get_object('com.spotify.qt', '/')
    iface = dbus.Interface(player, 'org.freedesktop.MediaPlayer2')
    info = iface.GetMetadata()
    try:
        return "Title: \t\t" + str(info['xesam:title'])+"\nArtist: \t\t" + str(info['xesam:artist'][0]) + "\nAlbum: \t" +  str(info['xesam:album'])
    except KeyError: #Sometimes songs in other languages screw up
        return ""

def notify():
    global current_track
    track_now = update()
    if track_now != current_track:
        current_track = track_now
        subprocess.Popen(['notify-send', '--expire-time=' + str(expire_time), '--icon=' + logo_abspath, update()])

while True:
    notify()
    time.sleep(update_time)
    



