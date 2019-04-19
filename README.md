# Ubuntu Crypto Price Ticker

Ubuntu Crypto Price Ticker is a simple price ticker widget for Linux Ubuntu
for showing the current price of any coin.

It was written on Ubuntu 17.10 and is a personal project of mine so
compatibility with other versions of Ubuntu may or may not work.

![Screenshot](https://raw.github.com/peter-featherstone/Ubuntu-Crypto-Price-Ticker/master/static/example.png)

## Installation
Install python dependencies by running the following command:
```
 make install
```
## Configuration
Configuration of tokens can be done by copying the `tokens-example.yaml` file
over to your own `tokens.yaml` file.

## Running
* Simply run `make` or `python3 app/main.py` to start the app

## Token Images
Token images are auto-downloaded from the coinmarketcap.com website each time
a new coin is added to the tokens.yaml file and doesn't already exist in the
repository. If you could be so kind as to push these up to the repo that would
be great and would serve others well.

## Contribution (Paras Lehana)

> Fork by paras-lehana

**Tweaks:**

* I have changed the decimal precison to none. If you want to include, remove `int` conversion in `self.widget.set_label` in `app/widgets.py` and change precison from 0 to (for example, back to) 2.
* You can add other configuration in example.yaml file by adding more commas. Be sure to use the fields in `__init__` in `app/widgets.py` after conf has been split. 
* Renamed `tokens-example.yaml` to `tokens.yaml` by default. Removed `tokens.yaml` from `.gitignore` as well due to added inline guide. Consider adding it again if you are pushing changes not related to it. 
* Do contact me for any more suggestion or additions. I'll be happy to add those. I'm grateful to peter-featherstone for this awesome widget.  

**Improved Guide:**

* You can find brief guide to help yourself adding new tokens in tokens.yaml.
* You need to define Token ID in the file as CMC API doesn't support symbols yet. 
* Token ids are generally same as coin name in lowercase. Replace space by hyphen in multiword token names. For example, `basic-attention-token` for Basic Attention Token (BAT)
* Find exact ids on CMC's token page url. For example, `coinmarketcap.com/currencies/basic-attention-token/`
* You can change refresh time in seconds by changing `REFRESH_TIME_IN_SECONDS` variable in `app/widget.py` file. Default is 10 mins so you may want to consider changing it. 
* If you want the script to autorun on startup, open 'Startup Applications' and type command `cd <installation_directory> && make` where installation_directory is the absolute path of the directory where you have forked my repo. There are others ways like /etc/init and startup scripts to do this too. 
* This repo by Peter Featherstone has many features so do ask me or post your queries by opening an Issue. I'll add the points here as well as promptly reply to the created ones. We need community help to make this project great again!


**Support for other conversion currencies including Satoshis:**

* I have added support for defining crypto-currencies and fiat as conversion currencies.
* Satoshi is also supported. Use 'SAT' for the same. For example, `bgogo-token,SAT`. 1 BTC equals 100 million Satoshis.
* You can define conversion currency as `<coin-id>,<conversion currency>`. For example, `Ethereum,INR` will show Ethereum price in Indian Rupees. 
* Both crypto-currency and fiat are supported for conversion as per CMC data. For example, you can use `Ripple,EUR` as well as `Ripple,BTC`.
* I have added a local array `currency_symbol` in `app/widget.py` file that countains symbol for different currencies (including crypto). Consider contributing into it or suggest me a suitable python library. I have used `シ` symbol for Satoshi. You change it to whatever you like. 

**Support for other conversion currencies including Satoshis:**

> April 19, 2019
> Discussion: https://github.com/peter-featherstone/Ubuntu-Crypto-Price-Ticker/pull/1#pullrequestreview-227912044

* I have added support for defining precision for displayed prices. 
* You can define precision after 2nd comma as `<coin-id>,<conversion currency>,<precision>`. For example, `Ethereum,USD,0` will show Ethereum price in US Dollars with 0 decimal places. So, a price of $172.11 will round off to $172.
* Default precision is 2 (two decimal places). 
* Make sure to put precision after 2 commas. `Bitcoin,,0` is also supported where conversion will be assumed default (USD).
