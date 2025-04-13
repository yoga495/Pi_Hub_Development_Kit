#!/usr/bin/env python3
import time
from gpiozero import MCP3008
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2

# Initialize MCP3008 ADC for Turbidity sensor on channel 2
turbidity_sensor = MCP3008(channel=2)

# Calibration values - adjust these based on your sensor and measurements
CLEAR_WATER = 0.57 # Value for clear water
UNTRETED_WATER = 0.3  # Value for very turbid water

try:
    print("Turbidity Sensor Test. Press CTRL+C to exit")    
    # Initial display
    lcd.lcd_clear()
    lcd.lcd_string("Turbidity Sensor", LCD_LINE_1)
    lcd.lcd_string("*****Test******", LCD_LINE_2)
    time.sleep(2)
    while True:
        # Read raw analog value (0 to 1.0)
        raw_value = turbidity_sensor.value
        print(f"rawvalue:{raw_value}")
        # Convert to NTU (Nephelometric Turbidity Units) - simplified calculation
        # Proper conversion depends on sensor calibration based on the raw value 
        if raw_value >= CLEAR_WATER:
            ntu = 0
        elif raw_value <= UNTRETED_WATER:
            ntu = 3000  # Highly turbid
        else:
            # Linear mapping between calibration points
            ntu = int((CLEAR_WATER - raw_value) / (CLEAR_WATER - UNTRETED_WATER) * 3000)
        
        # Display on LCD
        
        print(f"Turbidity: {ntu} NTU")
         # Display status message
        # Initial display
        lcd.lcd_clear()
        lcd.lcd_string(f"Turbidity: {ntu} NTU", LCD_LINE_1)
        
        # Display water quality
        
        if ntu < 5:
            print("Quality: CLEAR")
            lcd.lcd_string("Quality: CLEAR", LCD_LINE_2)
        elif ntu < 500:
            print("Quality: CLOUDY")
            lcd.lcd_string("Quality: CLOUDY", LCD_LINE_2)
        else:
            print("Quality: UNTRETED_WATER")
            lcd.lcd_string("Quality:UNTRETED", LCD_LINE_2)
        
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Test ended")
    lcd.lcd_clear()
    lcd.lcd_string("Test ended", LCD_LINE_1)
    time.sleep(1)
    
    
    
finally:
    # Clean up
    lcd.lcd_clear()
    time.sleep(1)
