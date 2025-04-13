#!/usr/bin/env python3
import time
from gpiozero import MotionSensor


# PIR sensor setup
PIR_PIN = 4  # GPIO4 as per  table
pir = MotionSensor(PIR_PIN)

def main():
    try:
        print("PIR Motion Sensor Test. Press CTRL+C to exit")


        
        # Allow PIR sensor to settle
        print("Initializing PIR sensor (10 seconds)...")
        time.sleep(10)        
        print("Ready to detect motion!")
        
        while True:
            if pir.motion_detected:
                print("Motion detected!")

                time.sleep(1)
            else:
                print("No Motion detected....")
                time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("Program stopped")
    finally:
        time.sleep(0.5)

if __name__ == "__main__":
    main()
