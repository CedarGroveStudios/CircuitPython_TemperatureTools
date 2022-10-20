# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: MIT
"""
`cedargrove_dew_point`
================================================================================

Calculate dew point from ambient temperature and humidity.


* Author(s): JG

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/CedarGroveStudios/CircuitPython_AirQualityTools.git"


# fmt: off

# Dew Point breakpoint list
#   Temperatures in Celsius
#   (dew point temperature minimum, maximum, summary, detail)
BREAKPOINTS = (
    (-9999,   10, "Safe", ": A bit dry for some."),
    (   10,   12, "Safe", ": Very comfortable."),
    (   13,   16, "Safe", ": Comfortable."),
    (   16,   18, "Safe", ": Okay for most."),
    (   18,   21, "Caution", ": Somewhat uncomfortable for most people."),
    (   21,   24, "Caution", ": Very humid, quite uncomfortable."),
    (   24,   26, "Extreme Caution", ": Extremely uncomfortable, fairly oppresive."),
    (   26, 9999, "DANGER", ": Severely high, potentially deadly for asthma sufferers."),
)

# fmt: on

# Dew Point converter (degrees Celsius)
def dew_point(deg_c, humidity, verbose=False):
    """Calculate dew point temperature from measured temperature (Celsius) and
    humidity (percent). Returns the calculated dew point (Celsius) and summary
    description. Detailed description is provided if verbose=True. Dew point
    value is constrained to the range of 0 to 40 (Celsius).

    :param float deg_c: The temperature in Celsius. No default.
    :param float humidity: The humidity in the range of 0 to 100
    percent. No default.
    :param bool verbose: The observation detail switch. False for summary; True
    for a detailed description. Defaults to False.
    """

    dew_point_c = round(
        (
            pow(humidity / 100.0, 0.125) * (112.0 + (0.9 * deg_c))
            + (0.1 * deg_c)
            - 112.0
        ),
        2,
    )

    # Constrain dew_point to range of 0 to 40 degrees Celsius
    dew_point_c = min(max(dew_point_c, 0), 40)

    # Select message from list
    for _, (_, maximum, summary, detail) in enumerate(BREAKPOINTS):
        if dew_point_c < maximum:
            if verbose:
                return dew_point_c, summary + detail
            return dew_point_c, summary

    return dew_point_c, "Invalid dew point value."
