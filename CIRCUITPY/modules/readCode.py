import board
import usb_host
import usb
import sys
import supervisor
import time



def readScanner():      
    while True:
        print(usb.core.find())
        print("Keyboard Reading...")
        print(sys.stdin.read(1))
        time.sleep(1)
