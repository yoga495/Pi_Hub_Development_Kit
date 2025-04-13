#!/usr/bin/env python3
from gpiozero import Servo
import time
import smbus



def main():

    
    # Configure servo motor
    # Servo is connected to GPIO12
    servo = Servo(12)
    
    try:
        while True:
            # Move servo to minimum position (-1)
            print("Servo Test" )
            print("Position: MIN" )
            servo.min()
            time.sleep(2)
            
            # Move servo to middle position (0)
            print("Servo Test" )
            print("Position: MID" )
            servo.mid()
            time.sleep(2)
            
            # Move servo to maximum position (1)
            print("Servo Test" )
            print("Position: MAX" )
            servo.max()
            time.sleep(2)
            
    except KeyboardInterrupt:
        # Clean up
        servo.close()
        print("Program ended" )
        time.sleep(1)
        

if __name__ == '__main__':
    main()
