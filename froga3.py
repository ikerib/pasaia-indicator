#!/usr/bin/env python3
import signal
import gi
import os
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

class Indicator():
    def __init__(self):
        self.app = 'test123'
        iconpath = os.path.abspath('asset/pasaia_logo.svg')
        # self.indicator = AppIndicator3.Indicator.new(self.app, iconpath, AppIndicator3.IndicatorCategory.OTHER)
        # self.indicator = AppIndicator3.Indicator.new(self.app, iconpath, AppIndicator3.IndicatorCategory.COMMUNICATIONS)
        # self.indicator = AppIndicator3.Indicator.new(self.app, iconpath, AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator = AppIndicator3.Indicator.new(self.app, iconpath, AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)       
        self.indicator.set_menu(self.create_menu())
        self.indicator.set_label("1 Monkey", self.app)

    def create_menu(self):
        menu = Gtk.Menu()
        # menu item 1
        item_1 = Gtk.MenuItem('Menu item')
        # item_about.connect('activate', self.about
        menu.append(item_1)
        # separator
        menu_sep = Gtk.SeparatorMenuItem()
        menu.append(menu_sep)
        # quit
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', self.stop)
        menu.append(item_quit)

        menu.show_all()
        return menu

    def stop(self, source):
        Gtk.main_quit()

Indicator()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()