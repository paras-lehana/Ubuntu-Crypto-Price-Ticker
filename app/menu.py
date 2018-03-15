#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
from config import PROJECT_ROOT
from gi.repository import AppIndicator3, Gtk, GdkPixbuf


class Menu(object):

    config = yaml.load(open(PROJECT_ROOT + '/config.yaml', 'r'))
    icon = PROJECT_ROOT + '/static/icon.png'

    def __init__(self):
        self.widget = AppIndicator3.Indicator.new(
            'Ubuntu Crypto Price Ticker Main',
            self.icon,
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS
        )
        self.widget.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.widget.set_menu(self._menu())

        self._set_label()

    def _set_label(self):
        self.widget.set_icon_full(self.icon, 'Main')

    def _menu(self):
        menu = Gtk.Menu()

        about = Gtk.MenuItem('About')
        about.connect('activate', self._about)
        menu.append(about)

        quit = Gtk.MenuItem('Quit')
        quit.connect('activate', self._quit)
        menu.append(quit)

        menu.show_all()

        return menu

    def _about(self, widget):
        about = Gtk.AboutDialog()

        about.set_program_name(self.config['app']['name'])
        about.set_comments(self.config['app']['description'])
        about.set_version(self.config['app']['version'])
        about.set_website(self.config['app']['url'])
        about.set_authors([
            '{} <{}>'.format(author['name'], author['email'])
            for author in self.config['authors']
        ])

        about.set_license_type(Gtk.License.MIT_X11)
        about.set_logo(GdkPixbuf.Pixbuf.new_from_file(self.icon))
        about.set_keep_above(True)
        about.run()

    def _quit(self, widget):
        Gtk.main_quit()
