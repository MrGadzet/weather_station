from machine import ADC, Pin, Timer, PWM, I2C
#from BMP280 import *
import time, onewire, ds18x20, ssd1306

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)

#bmp = BMP280(i2c)

#bmp.temp_os = BMP280_TEMP_OS_SKIP
#bmp.press_os = BMP280_PRES_OS_SKIP

#bmp.standby = BMP280_STANDBY_250
#bmp.iir = BMP280_IIR_FILTER_OFF

#bmp.power_mode = BMP280_POWER_NORMAL

adc1 = ADC(Pin(26))
adc2 = ADC(Pin(27))

ow = onewire.OneWire(Pin(22)) # create a OneWire bus on GPIO22
ds = ds18x20.DS18X20(ow)
dallas_t = None

#print("Temp. BMP", bmp.temperature)
#print("Pres. BMP", bmp.pressure)
#pwm = PWM(Pin(25))
#pwm.freq(100000)

while True:
    mos1 = adc1.read_u16()
    mos2 = adc2.read_u16()
    precent_mos1 = int(100-(mos1*100/65025))
    precent_mos2 = int(100-(mos2*100/65025))
    roms = ds.scan()
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        dallas_t = round(ds.read_temp(rom), 2)
        print("Temp. Dallas:", dallas_t, "*C")
    
#    bmp_t = round(bmp.temperature, 2)
#    bmp_p = round (bmp.pressure/100, 2)
#    bmp_p = bmp_p/100
#    print("Temp. BMP", bmp_t, "*C")
#    print("Pres. BMP", bmp_p, "hPa")
#    pwm.duty_u16(duty)
    print("Wilgotność 1:", "Raw:", mos1, "%", precent_mos1)
    print("Wilgotność 2:", "Raw:", mos2, "%", precent_mos2)
    
    def disp_t_p():
        display.fill(0)
#        display.text(f"t(bmp): {bmp_t, 2}*C", 0, 0, 1)
        display.text(f"T: {dallas_t}*C", 0, 1, 1)
        display.text(f"H1(g): {precent_mos1}%", 0, 10, 1)
        display.text(f"H2(g): {precent_mos2}%", 0, 20, 1)
#        display.text(f"p: {bmp_p}hPa", 0, 20, 1)
        display.show()
    
#    def disp_mos():
#        display.fill(0)
#        display.text(f"Cz1: {precent_mos1}%", 0, 0, 1)
#        display.text(f"Cz2: {precent_mos2}%", 0, 50, 1)
#        displat.show()
    
#    time_start = time.ticks_ms()
#    delta_time = time.diff(time.ticks_ms(), start)
#    if delta_time < = 5000:
    disp_t_p()
#    time.sleep_ms(20)