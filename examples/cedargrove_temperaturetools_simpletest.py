# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: Unlicense

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
