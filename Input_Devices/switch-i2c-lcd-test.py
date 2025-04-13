#!/usr/bin/env python3
import time
from gpiozero import Button
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2

# Switch setup
SW1_PIN = 22  # GPIO22 as per your table
SW2_PIN = 27  # GPIO27 as per your table
switch1 = Button(SW1_PIN, pull_up=True)  # Using pull-up, connect other side to GND
switch2 = Button(SW2_PIN, pull_up=True)  # Using pull-up, connect other side to GND

def main():
    try:
        print("Switch Sensor Test. Press CTRL+C to exit")
        
        # Initial display
        lcd.lcd_clear()
        lcd.lcd_string("Switch Sensor", LCD_LINE_1)
        lcd.lcd_string("Test", LCD_LINE_2)
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
            
            # Update LCD
            lcd.lcd_clear()
            lcd.lcd_string(f"SW1: {sw1_state}", LCD_LINE_1)
            lcd.lcd_string(f"SW2: {sw2_state}", LCD_LINE_2)
            
            # Print to terminal
            print(f"Switch 1: {sw1_state}, Switch 2: {sw2_state}")
            
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("Program stopped")
    finally:
        lcd.lcd_clear()

def switch_event(switch_name, state):
    print(f"{switch_name} {state}")

if __name__ == "__main__":
    main()
