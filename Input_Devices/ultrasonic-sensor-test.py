#!/usr/bin/env python3
import time
from gpiozero import DistanceSensor

# Ultrasonic sensor setup
TRIG_PIN = 5  # GPIO5 
ECHO_PIN = 6  # GPIO6 
ultrasonic = DistanceSensor(ECHO_PIN,TRIG_PIN)



def main():
    try:
        print("Ultrasonic Distance Sensor Test. Press CTRL+C to exit")
        
  
        while True:
            # Read distance
            distance = ultrasonic.distance * 100  # Convert to cm
            
            # Display on terminal
            print(f"Distance: {distance:.1f} cm")
            
            
            # Wait before next reading
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("Program stopped")
    finally:
        time.sleep(0.5)

if __name__ == "__main__":
    main()
