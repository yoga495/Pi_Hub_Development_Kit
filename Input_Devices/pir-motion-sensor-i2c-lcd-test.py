#!/usr/bin/env python3
import time
from gpiozero import MotionSensor
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2

# PIR sensor setup
PIR_PIN = 4  # GPIO4 as per  table
pir = MotionSensor(PIR_PIN)

def main():
    try:
        print("PIR Motion Sensor Test. Press CTRL+C to exit")
        
        # Initial display
        lcd.lcd_clear()
        lcd.lcd_string("PIR Motion", LCD_LINE_1)
        lcd.lcd_string("Sensor Test", LCD_LINE_2)
        time.sleep(2)
        
        # Allow PIR sensor to settle
        print("Initializing PIR sensor (10 seconds)...")
        lcd.lcd_clear()
        lcd.lcd_string("Initializing", LCD_LINE_1)
        lcd.lcd_string("Sensor...", LCD_LINE_2)
        time.sleep(10)
        
        print("Ready to detect motion!")
        lcd.lcd_clear()
        lcd.lcd_string("Motion Sensor", LCD_LINE_1)
        lcd.lcd_string("Ready!", LCD_LINE_2)
        
        while True:
            if pir.motion_detected:
                print("Motion detected!")
                lcd.lcd_clear()
                lcd.lcd_string("MOTION", LCD_LINE_1)
                lcd.lcd_string("DETECTED!", LCD_LINE_2)
                time.sleep(1)
            else:
                lcd.lcd_clear()
                lcd.lcd_string("No Motion", LCD_LINE_1)
                lcd.lcd_string("Detected", LCD_LINE_2)
                time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("Program stopped")
    finally:
        lcd.lcd_clear()

if __name__ == "__main__":
    main()
