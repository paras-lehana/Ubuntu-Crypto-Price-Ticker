#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import abspath, dirname, isfile
import yaml
from gi.repository import Gtk, GLib, GdkPixbuf, GObject
try:
    from gi.repository import AppIndicator3 as AppIndicator
except ImportError:
    from gi.repository import AppIndicator


import requests

import urllib, re

PROJECT_ROOT = abspath(dirname(dirname(__file__)))
PRICE_API = 'https://api.coinmarketcap.com/v1/ticker/{}/?convert=USD'
IMAGE_PAGE_URL = 'https://coinmarketcap.com/currencies/{}/'
IMAGE_URL = 'https://s2.coinmarketcap.com/static/img/coins/32x32/\d+.png'
REFRESH_TIME_IN_SECONDS = 600


class Widget(object):

    config = yaml.load(open(PROJECT_ROOT + '/config.yaml', 'r'))
    config['project_root'] = PROJECT_ROOT
    icon = config['project_root'] + '/static/icon.png'

    def __init__(self, main, token):
        self.main = main
        self.token = token.lower()

    def start(self):
        self.widget = AppIndicator.Indicator.new(
            "Ubuntu Crypto Price Ticker" + self.token, 
            self.icon, 
            AppIndicator.IndicatorCategory.APPLICATION_STATUS
        )
        self.widget.set_status(AppIndicator.IndicatorStatus.ACTIVE)
        self.widget.set_menu(self._menu())

        self._set_label_image()
        self._set_price()

    def stop(self):
        del self.widget

        if self.timeout_id:
            GLib.source_remove(self.timeout_id)

    def _set_label_image(self):
        token_image_location = '{}/static/token_icons/{}.png'.format(
            self.config['project_root'], self.token
        )

        if not isfile(token_image_location):
            response = requests.get(IMAGE_PAGE_URL.format(self.token))
            html = response.text

            for link in re.findall(IMAGE_URL, html):
                urllib.request.urlretrieve(link, token_image_location)

        self.widget.set_icon_full(token_image_location, self.token)

    def _set_price(self):
        response = requests.get(PRICE_API.format(self.token))
        token_data = response.json()[0]

        self.widget.set_label(
            ' ${}'.format(round(float(token_data['price_usd']), 2)),
            self.token
        )

        self.timeout_id = GLib.timeout_add_seconds(
            REFRESH_TIME_IN_SECONDS, self._set_price
        )

    def _menu(self):
        self.menu = Gtk.Menu()

        self.about_item = Gtk.MenuItem("About")
        self.quit_item = Gtk.MenuItem("Remove")

        self.about_item.connect("activate", self._about)
        self.quit_item.connect("activate", self._quit)

        self.menu.append(self.about_item)
        self.menu.append(Gtk.SeparatorMenuItem())
        self.menu.append(self.quit_item)
        self.menu.show_all()

        return self.menu

    def _about(self, widget):
        about = Gtk.AboutDialog()
        about.set_program_name(self.config['app']['name'])
        about.set_comments(self.config['app']['description'])
        about.set_version(self.config['app']['version'])
        about.set_website(self.config['app']['url'])
        authors = []
        for author in self.config['authors']:
            authors.append(author['name'] + ' <' + author['email'] + '>')
        about.set_authors(authors)

        about.set_license_type(Gtk.License.MIT_X11)
        about.set_logo(GdkPixbuf.Pixbuf.new_from_file(self.icon))
        about.set_keep_above(True)
        about.run()

    def _quit(self, widget):
        self.main._remove_ticker(self.token)
