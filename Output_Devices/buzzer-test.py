#!/usr/bin/env python3
from gpiozero import Buzzer
import time
import smbus


def main():
    # Configure buzzer
    # Buzzer is connected to GPIO25
    buzzer = Buzzer(25)
    
    try:
        while True:
            # Turn on buzzer
            print("Buzzer Test" )
            print("Status: ON" )
            buzzer.on()
            time.sleep(2)
            
            # Turn off buzzer
            print("Buzzer Test" )
            print("Status: OFF" )
            buzzer.off()
            time.sleep(2)
            
            # Beep pattern
            print("Buzzer Test" )
            print("Status: BEEPING" )
            for _ in range(5):
                buzzer.on()
                time.sleep(0.1)
                buzzer.off()
                time.sleep(0.1)
            time.sleep(1)
            
    except KeyboardInterrupt:
        # Clean up
        buzzer.off()
        buzzer.close()
        print("Program ended" )
        time.sleep(1)

if __name__ == '__main__':
    main()
