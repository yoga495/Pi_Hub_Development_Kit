#!/usr/bin/env python3
from gpiozero import RGBLED
import time
import smbus


def main():

    
    # Configure RGB LED using GPIO pins
    # RGB LED is connected to GPIO13 (B), GPIO26 (G), GPIO19 (R)
    rgb_led = RGBLED(red=19, green=26, blue=13)
    
    try:
        while True:
            # Red
            rgb_led.color = (1, 0, 0)  # Full red
            print("RGB LED Test")
            print("Color: RED")
            time.sleep(2)
            
            # Green
            rgb_led.color = (0, 1, 0)  # Full green
            print("RGB LED Test")
            print("Color: GREEN" )
            time.sleep(2)
            
            # Blue
            rgb_led.color = (0, 0, 1)  # Full blue
            print("RGB LED Test" )
            print("Color: BLUE" )
            time.sleep(2)
            
            # Purple (Red + +Green +Blue)
            rgb_led.color = (1, 1, 1)  # White
            print("RGB LED Test" )
            print("Color: White" )
            time.sleep(2)
            
            # Off
            rgb_led.off()
            print("RGB LED Test" )
            print("LED: OFF" )
            time.sleep(1)
            
    except KeyboardInterrupt:
        # Clean up
        rgb_led.close()
        print("Program ended" )
        time.sleep(1)


if __name__ == '__main__':
    main()
