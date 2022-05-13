import machine, onewire, ds18x20, time
dat = machine.Pin(2)
ds = ds18x20.DS18X20(onewire.OneWire(dat))
tim = machine.Timer(-1)
tim2 = machine.Timer(-1)
roms = ds.scan()
print(roms)
temp = 0
 
def getTemp(p):
    global temp
    temp = round(ds.read_temp(roms[0]))
 
def startConv(p = 0):
    ds.convert_temp()
    print(temp)
    time.sleep(1)
    tim2.init(period=750, mode=machine.Timer.ONE_SHOT, callback=getTemp)
 
startConv()
tim.init(period=1, mode=machine.Timer.PERIODIC, callback=startConv)
