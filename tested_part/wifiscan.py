import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
#wifi = sta_if.scan()
for x in sta_if.scan(): print(x)           # Scan for available access points
#sta_if.connect("<AP_name>", "<password>") # Connect to an AP
#sta_if.isconnected()                      # Check for successful connection
