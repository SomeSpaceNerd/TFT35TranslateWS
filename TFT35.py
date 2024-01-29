import serial
import requests
import json
import time
import config
import TFTrst

RS232 = serial.Serial('/dev/serial0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
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
