import microcontroller

microcontroller.cpu.frequency = 120000000
print(microcontroller.cpu.frequency)


import os
import wifi

import board
import usb_host
import usb
import sys
import supervisor
import time

import ssl
import socketpool
import json
import adafruit_requests 

# Get WiFi details, ensure these are setup in settings.toml
ssid = os.getenv("CIRCUITPY_WIFI_SSID")
password = os.getenv("CIRCUITPY_WIFI_PASSWORD")

# Initialize WiFi Pool 
radio = wifi.radio
pool = socketpool.SocketPool(radio)

while not wifi.radio.ipv4_address:
    try:
        wifi.radio.connect(ssid, password)
    except ConnectionError as e:
        print("could not connect to AP, retrying: ", e)


# Initialize a requests session
ssl_context = ssl.create_default_context()
requests = adafruit_requests.Session(pool, ssl_context)

#Wireless conection
POST_URL = os.getenv("POST_URL")

#init DPIO
usb_host.Port(board.GP0, board.GP1)

if supervisor.runtime.usb_connected:
    print("USB conected")
else:
    print("USB not connected")
    
while True:
    scannerAccumulator = ""
    data = {}
    while True:
            ScanInput = sys.stdin.read(1)
            scannerAccumulator += ScanInput
            if ScanInput == "\n":
                break
    if len(scannerAccumulator) == 9 :
        print(scannerAccumulator)
       
        data["RA"] = scannerAccumulator[:-1]
        print(json.dumps(data))
        requests.post(POST_URL,data=json.dumps(data))
        
    

