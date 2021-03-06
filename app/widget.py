#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib

import requests
from config import PROJECT_ROOT
from gi.repository import AppIndicator3, GLib, Gtk
from os.path import isfile

PRICE_API = 'https://api.coinmarketcap.com/v1/ticker/{}/?convert={}'
IMAGE_PAGE_URL = 'https://coinmarketcap.com/currencies/{}/'
IMAGE_URL = 'https://s2.coinmarketcap.com/static/img/coins/64x64/\d+.png'
REFRESH_TIME_IN_SECONDS = 10

currency_symbol = dict(usd='$', eur='€', inr='₹', btc='฿', eth='Ξ',sat='シ')

class Widget(object):

    icon = PROJECT_ROOT + '/static/icon.png'

    def __init__(self, token):
        conf = token.split(',')

        self.token = conf[0].lower()
        self.convert = conf[1].lower() if len(conf) > 1 and len(conf[1]) else 'usd'
        self.precision = int(conf[2].lower()) if len(conf) > 2 and len(conf[2]) else 2
        self.widget = AppIndicator3.Indicator.new(
            "Ubuntu Crypto Price Ticker {}".format(self.token),
            self.icon, 
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS
        )
        self.widget.set_status(
            AppIndicator3.IndicatorStatus.ACTIVE
        )
        self.widget.set_menu(Gtk.Menu())

        self._set_label_image()
        self._set_price()

    def _set_label_image(self):
        token_image_location = '{}/static/token_icons/{}.png'.format(
            PROJECT_ROOT, self.token
        )
        if not isfile(token_image_location):
            response = requests.get(IMAGE_PAGE_URL.format(self.token))
            html = response.text
            for link in re.findall(IMAGE_URL, html):
                urllib.request.urlretrieve(link, token_image_location)
                

        self.widget.set_icon_full(token_image_location, self.token)

    def _set_price(self):
        response = requests.get(PRICE_API.format(self.token,self.convert))
        token_data = response.json()[0]

        token_key = 'price_btc' if self.convert == 'sat' else 'price_' + str(self.convert)
        amount = float(token_data[token_key]) * (100000000 if self.convert == 'sat' else 1)
        display_price =  int(round(float(amount), self.precision)) if self.precision == 0 else round(float(amount), self.precision)
        price_string = ' {}{}'.format(
            currency_symbol.get(self.convert, ''),display_price)

        self.widget.set_label(price_string, self.token)

        self.timeout_id = GLib.timeout_add_seconds(
            REFRESH_TIME_IN_SECONDS, self._set_price
        )

    def resume(self):
        self._set_price()
