try:
  import usocket as socket
except:
  import socket

import network
import esp
import gc

esp.osdebug(None)
gc.collect()


