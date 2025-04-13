#!/usr/bin/env python3
import time
from gpiozero import Button

# Switch setup
SW1_PIN = 22  # GPIO22 as per your table
SW2_PIN = 27  # GPIO27 as per your table
switch1 = Button(SW1_PIN, pull_up=True)  # Using pull-up, connect other side to GND
switch2 = Button(SW2_PIN, pull_up=True)  # Using pull-up, connect other side to GND

def main():
    try:
        print("Switch Sensor Test. Press CTRL+C to exit")
        time.sleep(2)
        
        # Set up event handlers
        switch1.when_pressed = lambda: switch_event("SW1", "PRESSED")
        switch1.when_released = lambda: switch_event("SW1", "RELEASED")
        switch2.when_pressed = lambda: switch_event("SW2", "PRESSED")
        switch2.when_released = lambda: switch_event("SW2", "RELEASED")
        
        # Main loop
        while True:
            # Get current switch states
            sw1_state = "CLOSED" if switch1.is_pressed else "OPEN"
            sw2_state = "CLOSED" if switch2.is_pressed else "OPEN"
            
            # Print to terminal
            print(f"Switch 1: {sw1_state}, Switch 2: {sw2_state}")
            
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("Program stopped")
    finally:
        time.sleep(0.1)

        

def switch_event(switch_name, state):
    print(f"{switch_name} {state}")

if __name__ == "__main__":
    main()
