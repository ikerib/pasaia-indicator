#!/usr/bin/env python3

import gi
import json
import os
import requests
import signal
import socket
import time
import urllib3

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk, AppIndicator3, GObject
from gi.repository import GLib as glib
from gi.repository import Notify as notify

from threading import Thread
from urllib.request import urlopen

APPINDICATOR_ID = 'Pasaiako Udala'

class Indicator():
    def __init__(self):
        self.app = APPINDICATOR_ID
        iconpath = os.path.abspath('asset/pasaia_logo32.png')
        self.indicator = AppIndicator3.Indicator.new(self.app, iconpath, AppIndicator3.IndicatorCategory.OTHER)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())
        notify.init(APPINDICATOR_ID)

        labela = "IP: " + Indicator.fetch_ip(self)
        self.indicator.set_label(labela, self.app)
    
        Gtk.main()

    def create_menu(self):
        menu = Gtk.Menu()

        # Joke
        item_joke = Gtk.MenuItem('Joke')
        item_joke.connect('activate', self.joke)
        menu.append(item_joke)

        # IP helbidea
        item_get_ip = Gtk.MenuItem('IP helbidea')
        item_get_ip.connect('activate', Indicator.get_ip)
        menu.append(item_get_ip)

        # VNC eskaera
        item_vnc = Gtk.MenuItem('VNC Eskaera')
        item_vnc.connect('activate', Indicator.notify_vnc)
        menu.append(item_vnc)

        # separator
        menu_sep = Gtk.SeparatorMenuItem()
        menu.append(menu_sep)

        # quit
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', quit)
        menu.append(item_quit)
        menu.show_all()

        return menu


    @staticmethod
    def joke(self):
        response2 = requests.get('http://api.icndb.com/jokes/random?limitTo=[nerdy]')
        joke = json.loads(response2.content.decode('utf-8'))['value']['joke']
        notify.Notification.new("Joke", joke, None).show()

    @staticmethod
    def fetch_ip(self):
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

    def get_ip(self):
        notify.Notification.new("IP", Indicator.fetch_ip(self), None).show()

    def notify_vnc(self):
        notify.Notification.new("VNC", 'Aukera honetan VNC eskaera', None).show()

    def quit(self):
        notify.uninit()
        Gtk.main_quit()

    def stop(self, source):
        Gtk.main_quit()


Indicator()
# this is where we call GObject.threads_init()
GObject.threads_init()
signal.signal(signal.SIGINT, signal.SIG_DFL)

