import serial
import requests
import json
import time
from websockets.sync.client import connect
import config
import TFTrst

RS232 = serial.Serial(str(config.ScreenInterface), baudrate=int(config.ScreenBaud), parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
Success = 0
SerialData = ""
Startup= 0
TFTrst.init()

while Startup == 0:
    r = requests.get(config.MoonrakerURL + "/server/info")
    StartupStatus = r.json()
    StartupConnected = StartupStatus["result"]["klippy_connected"]
    if str(StartupConnected) == "True":
        Startup = 1
        time.sleep(1)
        TFTrst.ResetTFT()

while True:
    time.sleep(0.1)
    BytesIn = RS232.inWaiting()
    if BytesIn > 0:
