#!/usr/bin/env python3
import os
import signal
import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, AppIndicator3, GObject
import time
from threading import Thread

# --- define what to show:
# showtime = textual time, daytime = a.m./p.m. period = "night"/"morning"/day"/"evening"
# speak = speak out time every quarter, fuzzy = round time on 5 minutes
showtime = True; daytime = False; period = True; speak = True; fuzzy = True

class Indicator():
    def __init__(self):
        self.app = 'about_time'
        path = os.path.dirname(os.path.abspath(__file__))
        self.indicator = AppIndicator3.Indicator.new(
            self.app, os.path.abspath('asset/pasaia_logo.svg'),
            AppIndicator3.IndicatorCategory.OTHER)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)       
        self.indicator.set_menu(self.create_menu())

        GObject.idle_add(
                self.indicator.set_label,
                "AAAAAAAAAAAAAA", self.app,
                priority=GObject.PRIORITY_DEFAULT
                )

        self.update = Thread(target=self.get_time)
        self.update.setDaemon(True)
        self.update.start()

    def get_time(self):
        print ("Hemen")
        GObject.idle_add(
                self.indicator.set_label,
                "AAAAAAAAAAAAAA", self.app,
                priority=GObject.PRIORITY_DEFAULT
                )

    def create_menu(self):
        menu = Gtk.Menu()
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', self.stop)
        menu.append(item_quit)
        menu.show_all()
        return menu

    def stop(self, source):
        Gtk.main_quit()

Indicator()
GObject.threads_init()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()