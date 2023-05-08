# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_ccs811

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
ccs811 = adafruit_ccs811.CCS811(i2c)

# Wait for the sensor to be ready
while not ccs811.data_ready:
    pass

while True:
    # Read CO2 and TVOC values
    co2 = ccs811.eco2
    tvoc = ccs811.tvoc

    # Write CO2 value to a file
    with open('/home/pi/sensores/sens_txt/eco2.txt', 'w') as f:
        f.write(str(co2))

    # Write TVOC value to a file
    with open('/home/pi/sensores/sens_txt/tvoc.txt', 'w') as f:
        f.write(str(tvoc))

    time.sleep(2)
