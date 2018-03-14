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