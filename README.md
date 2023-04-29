# Raspberry Pi Pico GPIO Pinout

A beautiful GPIO pinout and pin function guide for the Raspberry Pi Pico.

![Example image](https://raw.githubusercontent.com/pinout-xyz/picopins/main/example.png)

[![Build Status](https://img.shields.io/github/actions/workflow/status/pinout-xyz/picopins/build.yml?branch=main)](https://github.com/pinout-xyz/picopins/actions/workflows/build.yml)
[![PyPi Package](https://img.shields.io/pypi/v/picopins.svg)](https://pypi.python.org/pypi/picopins)
[![Python Versions](https://img.shields.io/pypi/pyversions/picopins.svg)](https://pypi.python.org/pypi/picopins)

# Usage

```
usage: picopins [--pins] [--all] or {spi,i2c,uart,pwm}
       --pins - show physical pin numbers
       --all or {spi,i2c,uart,pwm} - pick list of interfaces to show
       --hide-gpio - hide GPIO pins
       --find "<text>" - highlight pins matching <text>

eg:    picopins i2c  - show GPIO and I2C labels
       picopins      - basic GPIO pinout
```

# Installing

* Just run `python3 -m pip install picopins`


# Web server

Using the built-in python web server, you can run your own zero configuration pinout server with

`python3 server.py`

*Dependancy*: please install `expect` package for your OS e.g. for  Debian based systems `sudo apt install expect` The script requires `unbuffer` command to preserve ANSI colors when outputting the text.

The webserver accepts the same parameters as the library but chained in the request url for example:

```
curl localhhost:8001/all
curl localhhost:8001/all/find-pwm0/
curl localhhost:8001/pins/i2c
```
