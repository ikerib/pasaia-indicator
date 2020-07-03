from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

import os
import signal
import json
import urllib3
from gi.repository import Notify as notify
from urllib.request import urlopen
import requests
import socket

APPINDICATOR_ID = 'Pasaiako Udala'

def main():
    # indicator = appindicator.Indicator.new(APPINDICATOR_ID, 'kaixooooooooo' ), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('asset/pasaia_logo.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    item_joke = gtk.MenuItem('Joke')
    item_joke.connect('activate', joke)
    menu.append(item_joke)

    item_get_ip = gtk.MenuItem('IP helbidea')
    item_get_ip.connect('activate', get_ip)
    menu.append(item_get_ip)

    item_vnc = gtk.MenuItem('Egin eskaria ordenagilua kontrolatzeko')
    item_vnc.connect('activate', notify_vnc)
    menu.append(item_vnc)

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def fetch_joke():
    response2 = requests.get('http://api.icndb.com/jokes/random?limitTo=[nerdy]')
    return json.loads(response2.content.decode('utf-8'))['value']['joke']

def fetch_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def joke(_):
    notify.Notification.new("Joke", fetch_joke() , None).show()

def get_ip(_):
    notify.Notification.new("IP", fetch_ip(), None).show()

def notify_vnc(_):
    notify.Notification.new("VNC", 'Aukera honetan VNC eskaera', None).show()

def quit(_):
    notify.uninit()
    gtk.main_quit() 

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()