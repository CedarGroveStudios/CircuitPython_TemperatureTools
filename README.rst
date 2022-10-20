Introduction
============




.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/CedarGroveStudios/CircuitPython_AirQualityTools/workflows/Build%20CI/badge.svg
    :target: https://github.com/CedarGroveStudios/CircuitPython_AirQualityTools/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A collection of CircuitPython helpers for calculating and converting temperature.


``Dew Point`` calculates dew point temperature from measured temperature (Celsius)
and humidity (percent). Returns the calculated dew point (Celsius) and summary
description. Detailed description is provided if ``verbose=True``. Dew point value
is constrained to the range of 0 to 40 (Celsius).

``Heat Index`` calculates heat index temperature from measured temperature
(Celsius) and humidity (percent). Returns the calculated heat index (Celsius)
and summary description. Detailed description is provided if ``verbose=True``.

``Unit Converters`` convert values between Celsius, Fahrenheit, and Kelvin.


.. image:: https://github.com/CedarGroveStudios/CircuitPython_AirQualityTools/blob/main/media/WARNING.jpg

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.


Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install cedargrove_temperaturetools

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    from cedargrove_temperaturetools.dew_point import dew_point
    from cedargrove_temperaturetools.heat_index import heat_index
    from cedargrove_temperaturetools.unit_converters import (
        celsius_to_fahrenheit,
        celsius_to_kelvin,
    )

    # Measured temperature and humidity
    TEMPERATURE = 24  # Degrees Celsius
    HUMIDITY = 50  # Relative humidity in percent

    dew_point_temp, description = dew_point(TEMPERATURE, HUMIDITY)
    print(f"Dew Point = {dew_point_temp} {description}")

    dew_point_temp, description = dew_point(TEMPERATURE, HUMIDITY, verbose=True)
    print(f"Dew Point = {dew_point_temp} {description}")

    heat_index_temp, description = heat_index(TEMPERATURE, HUMIDITY)
    print(f"Heat Index = {heat_index_temp} {description}")

    heat_index_temp, description = heat_index(TEMPERATURE, HUMIDITY, verbose=True)
    print(f"Heat Index = {heat_index_temp} {description}")

    print(f"Measured Temperature (Celsius) = {TEMPERATURE}")
    print(f"Measured Temperature (Fahrenheit) = {celsius_to_fahrenheit(TEMPERATURE)}")
    print(f"Measured Temperature (Kelvin) = {celsius_to_kelvin(TEMPERATURE)}")



Documentation
=============
API documentation for this library can be found on `Read the Docs <https://github.com/CedarGroveStudios/CircuitPython_TemperatureTools/blob/main/media/pseudo_rtd_temperaturetools.pdf/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/CedarGroveStudios/CircuitPython_AirQualityTools/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
