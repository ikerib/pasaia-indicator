import json
import os
import signal
import urllib3
import requests
import socket

from gi.repository import AppIndicator3 as appindicator
from gi.repository import GLib as glib
from gi.repository import Gtk as gtk
from gi.repository import Notify as notify

from urllib.request import urlopen

APPINDICATOR_ID = 'Pasaiako Udala'
ind = None

def main():
    # indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('asset/pasaia_logo.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    # indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    # indicator.set_menu(build_menu())
    ind = appindicator.Indicator.new("example-simple-client",os.path.abspath('asset/pasaia_logo.svg'),appindicator.IndicatorCategory.APPLICATION_STATUS)
    ind.set_status (appindicator.IndicatorStatus.ACTIVE)
    ind.set_label('NA', '')
    ind.set_label('kokokokokokok' , '')
    ind.set_icon_full(os.path.abspath('asset/pasaia_logo.svg'), 'Play')
    ind.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    update(ind)
    # glib.timeout_add_seconds( 3, update(ind))
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    item_joke = gtk.MenuItem('Joke')
    item_joke.connect('activate', joke)
    menu.append(item_joke)

    item_get_ip = gtk.MenuItem('IP helbidea')
    item_get_ip.connect('activate', get_ip)
    menu.append(item_get_ip)

    item_vnc = gtk.MenuItem('VNC Eskaera')
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

def update_ind_label():
    value = glib.timeout_add_seconds(5, handler_timeout)

def update(ind):
        ind.set_label("LPLPLPLP","")

        #        self.indicator.set_label( "static label", "" ) # Using a static label, the icon does not change unless clicked with the mouse.
        # self.indicator.set_label( str( self.count ), "" ) # Using a dynamic label (which does not repeat) DOES change the icon.

        # self.count += 1

        return True


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    # main()
    try:
        thread.start_new_thread(update_ind_label, ())
    except:
        print ("Error: unable to start thread")

    main()
