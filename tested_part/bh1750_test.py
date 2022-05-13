from machine import I2C, Pin
from bh1750 import *
from utime import sleep_ms

# init eps8266 i2c
i2c = I2C(0, scl=Pin(5), sda=Pin(4))

s = BH1750(i2c)

while True:
    print(int(s.luminance(BH1750.CONT_HIRES_1)))
#    sleep_ms(200) 