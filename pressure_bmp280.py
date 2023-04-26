from bmp_280 import BMP280
from time import sleep
import math
#import smbus
#import time

#bus = smbus.SMBus(1)
#time.sleep(1)

bmp = BMP280(port=1, mode=BMP280.FORCED_MODE, oversampling_p=BMP280.OVERSAMPLING_P_x16,
oversampling_t=BMP280.OVERSAMPLING_T_x1, filter=BMP280.IIR_FILTER_OFF, standby=BMP280.T_STANDBY_1000)

pressure = bmp.read_pressure()
temp = bmp.read_temperature()

sea_level_pressure = 1013.25  # Presión al nivel del mar en hPa
altitude = 44330.0 * (1 - (pressure / sea_level_pressure) ** (1/5.255))

#def altitude(pressure):
#    return round((1 - (pressure / 1013.25)**0.190284) * 44307.69396, 2)

#altitude = altitude(pressure)

print("Altitude (m): " + str(altitude))
print("Pressure (hPa): " + str(pressure))
#print("Temperature (°C): " + str(temp))
