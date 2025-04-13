#!/usr/bin/env python3
import time
from gpiozero import DistanceSensor
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2

# Ultrasonic sensor setup
TRIG_PIN = 5  # GPIO5 
ECHO_PIN = 6  # GPIO6 
ultrasonic = DistanceSensor(ECHO_PIN,TRIG_PIN)



def main():
    try:
        print("Ultrasonic Distance Sensor Test. Press CTRL+C to exit")
        
        # Initial display
        lcd.lcd_clear()
        lcd.lcd_string("Ultrasonic", LCD_LINE_1)
        lcd.lcd_string("Distance Sensor", LCD_LINE_2)
        time.sleep(2)
        
        while True:
            # Read distance
            distance = ultrasonic.distance * 100  # Convert to cm
            
            # Display on terminal
            print(f"Distance: {distance:.1f} cm")
            
            # Display on LCD
            lcd.lcd_clear()
            lcd.lcd_string("Distance:", LCD_LINE_1)
            lcd.lcd_string(f"{distance:.1f} cm", LCD_LINE_2)
            
            # Wait before next reading
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("Program stopped")
    finally:
        lcd.lcd_clear()

if __name__ == "__main__":
    main()
