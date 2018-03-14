#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import signal
import yaml

from os.path import abspath, dirname, isfile

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk

try:
    from gi.repository import AppIndicator3 as AppIndicator
except ImportError:
    from gi.repository import AppIndicator
from widget import Widget


class Main(object):

    TOKENS_FILE_LOCATION = abspath(dirname(dirname(__file__))) + '/tokens.yaml'

    def __init__(self):
        if isfile(self.TOKENS_FILE_LOCATION):
            yaml_tokens = yaml.load(open(self.TOKENS_FILE_LOCATION, 'r'))
            self.tokens = yaml_tokens.get('tokens').split(' ')

        self.widgets = {}
        self._start()

    def _start(self):
        self._add_tickers()

    def _add_tickers(self):
        for token in self.tokens:
            widget = self._add_ticker(token)
            self.widgets.update({widget.token: widget})

    def _add_ticker(self, token):
        widget = Widget(self, token)
        widget.start()
        return widget

    def _remove_ticker(self, token):
        if len(self.widgets) is 1:
            Gtk.main_quit()
        else:
            self.widgets[token].stop()

        del self.widgets[token]


if __name__ == '__main__':
    Main()
    signal.signal(signal.SIGINT, Gtk.main_quit)
    Gtk.main()
