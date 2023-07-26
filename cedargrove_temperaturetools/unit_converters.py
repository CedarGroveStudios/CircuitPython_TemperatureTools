# SPDX-FileCopyrightText: Copyright (c) 2023 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: MIT
"""
`cedargrove_temperature`
================================================================================

A collection of temperature converters.


* Author(s): JG

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/CedarGroveStudios/CircuitPython_TemperatureTools.git"


def celsius_to_fahrenheit(deg_c):
    """Convert degrees Celsius to degrees Fahrenheit.

    :param float deg_c: The temperature in Celsius. No default.
    """
    return ((9 / 5) * deg_c) + 32


def fahrenheit_to_celsius(deg_f):
    """Convert degrees Fahrenheit to degrees Celsius.

    :param float deg_f: The temperature in Fahrenheit. No default.
    """
    return (deg_f - 32) * (5 / 9)


def celsius_to_kelvin(deg_c):
    """Convert degrees Celsius to Kelvin.

    :param float deg_c: The temperature in Celsius. No default.
    """
    return deg_c + 273.15


# Kelvin to Celsius converter
def kelvin_to_celsius(kelvins):
    """Convert Kelvin to degrees Celsius.

    :param float kelvins: The temperature in Kelvin. No default.
    """
    return kelvins - 273.15
