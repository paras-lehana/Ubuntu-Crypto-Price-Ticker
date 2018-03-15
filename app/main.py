#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import signal

import yaml
from gi.repository import Gtk
from menu import Menu
from os.path import abspath, dirname
from widget import Widget

import dbus
from dbus.mainloop.glib import DBusGMainLoop


class Main(object):

    TOKENS_FILE_LOCATION = abspath(dirname(dirname(__file__))) + '/tokens.yaml'

    def __init__(self):
        yaml_tokens = yaml.load(open(self.TOKENS_FILE_LOCATION, 'r'))
        self.tokens = yaml_tokens.get('tokens').split(' ')
        self.tickers = []

        self._add_main_menu()
        self._add_tickers()

    def resume(self, sleeping):
        if not sleeping:
            for ticker in self.tickers:
                ticker.resume()

    def _add_tickers(self):
        for token in self.tokens:
            self.tickers.append(Widget(token))

    def _add_main_menu(self):
        Menu()


if __name__ == '__main__':
    main = Main()
    signal.signal(signal.SIGINT, Gtk.main_quit)
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    bus.add_signal_receiver(
        main.resume,
        None,
        'org.freedesktop.login1.Manager',
        'org.freedesktop.login1'
    )
    Gtk.main()
