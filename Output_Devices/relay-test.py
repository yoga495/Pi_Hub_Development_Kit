#!/usr/bin/env python3
from gpiozero import OutputDevice
import time
import smbus


def main():

    
    # Configure relay pins
    # Relay IN1 connected to GPIO23, IN2 connected to GPIO24
    relay1 = OutputDevice(24, active_high=False)  # Set active_high=False if relay is active LOW
    relay2 = OutputDevice(23, active_high=False)  # Set active_high=False if relay is active LOW
    
    try:
        while True:
            # Turn on relay 1
            print("Relay Test" )
            print("Relay 1: ON" )
            relay1.on()
            relay2.off()
            time.sleep(2)
            
            # Turn on relay 2
            print("Relay Test" )
            print("Relay 2: ON" )
            relay1.off()
            relay2.on()
            time.sleep(2)
            
            # Turn on both relays
            print("Relay Test" )
            print("Both Relays: ON" )
            relay1.on()
            relay2.on()
            time.sleep(2)
            
            # Turn off both relays
            print("Relay Test" )
            print("Both Relays: OFF" )
            relay1.off()
            relay2.off()
            time.sleep(2)
            
    except KeyboardInterrupt:
        # Clean up
        relay1.off()
        relay2.off()
        relay1.close()
        relay2.close()
        print("Program ended" )
        time.sleep(1)
       

if __name__ == '__main__':
    main()
