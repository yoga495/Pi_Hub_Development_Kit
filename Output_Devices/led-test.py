#!/usr/bin/env python3
from gpiozero import LED
import time
import smbus



def main():

    # Configure LED pins
    led1 = LED(18)  # GPIO18 for LED1
    led2 = LED(16)  # GPIO16 for LED2

    try:
        while True:
            # Turn on LEDs
            led1.on()
            led2.on()
            print("LED Test")    
            print("LED1:OFF,LED2: ON")
            time.sleep(2)
            
            # Turn off LEDs
            led1.off()
            led2.off()
            print("LED Test")
            print("LED1:ON,LED2: OFF")
            time.sleep(2)

    except KeyboardInterrupt:
        # Clean up
        led1.close()
        led2.close()
        print("Program ended")
        time.sleep(1)
        

if __name__ == '__main__':
    main()
