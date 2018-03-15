#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import signal

import yaml
from gi.repository import Gtk
from menu import Menu
from os.path import abspath, dirname
from widget import Widget


class Main(object):

    TOKENS_FILE_LOCATION = abspath(dirname(dirname(__file__))) + '/tokens.yaml'

    def __init__(self):
        yaml_tokens = yaml.load(open(self.TOKENS_FILE_LOCATION, 'r'))
        self.tokens = yaml_tokens.get('tokens').split(' ')

        self._add_main_menu()
        self._add_tickers()

    def _add_main_menu(self):
        Menu()

    def _add_tickers(self):
        for token in self.tokens:
            Widget(token)


if __name__ == '__main__':
    Main()
    signal.signal(signal.SIGINT, Gtk.main_quit)
    Gtk.main()
