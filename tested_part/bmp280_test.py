import time, ssd1306, onewire, ds18x20
from machine import I2C, Pin
from bmp280 import *

temp = None
pres = None

dat = Pin(2)
ds = ds18x20.DS18X20(onewire.OneWire(dat))

#print(roms)
temp_ds = 0

bus = I2C(sda=Pin(4), scl=Pin(5))
bmp = BMP280(bus)

display = ssd1306.SSD1306_I2C(128, 32, bus)
display.text("Czujnik temp", 0, 0, 1)
display.text(" i cisnienia", 0, 10, 1)
display.show()
time.sleep(1)
bmp.temp_os =BMP280_TEMP_OS_2
bmp.press_os = BMP280_PRES_OS_2

bmp.standby = BMP280_STANDBY_250
bmp.iir = BMP280_IIR_FILTER_OFF

bmp.power_mode = BMP280_POWER_NORMAL

def dallas_temp():
    roms = ds.scan()
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        global temp_ds
        temp_ds = ds.read_temp(rom)
        #print(temp_ds)

while True:
    temp = bmp.temperature
    pres = bmp.pressure
    #print('Temperatura:', temp)
    #print('Ciśnienie:', pres)
#   startConv()
#   tim.init(period=1, mode=machine.Timer.PERIODIC, callback=startConv)
    
    dallas_temp()
    display.fill(0)
    display.text("T:" + str(temp), 0, 0, 1)
    display.text("P:" + str(pres), 0, 10, 1)
    display.text("T(ds):" + str(temp_ds), 0, 20, 1)
    display.show()
    #time.sleep_ms(50)

