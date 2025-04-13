#!/usr/bin/env python3
import time
from gpiozero import MCP3008
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2

# Initialize MCP3008 ADC for Moisture sensor on channel 0
moisture_sensor = MCP3008(channel=0)

# Calibration values - adjust these based on your sensor and soil type
# These values need to be calibrated for your specific soil and sensor
DRY_VALUE = 0.8  # Value when sensor is in dry air
WET_VALUE = 0.2  # Value when sensor is in water

try:
    print("Moisture Sensor Test. Press CTRL+C to exit")
    # Initial display
    lcd.lcd_clear()
    lcd.lcd_string("Moisture Sensor", LCD_LINE_1)
    lcd.lcd_string("*****Test******", LCD_LINE_2)
    time.sleep(2)
    
    while True:
        # Read raw analog value (0 to 1.0)
        raw_value = moisture_sensor.value
        print(moisture_sensor.value)
        # Convert to percentage (0% = dry, 100% = wet)
        if raw_value >= DRY_VALUE:
            moisture_percent = 100
        elif raw_value <= WET_VALUE:
            moisture_percent = 0
        else:
            moisture_percent = int((DRY_VALUE - raw_value) / (DRY_VALUE - WET_VALUE) * 100)
        

        print(f"Moisture: {moisture_percent}%")
        
        # Display status message
        # Initial display
        lcd.lcd_clear()
        lcd.lcd_string(f"Moisture: {moisture_percent}%", LCD_LINE_1)
        
        
        if moisture_percent < 30:
            print("Status: WET")
            lcd.lcd_string("Status: WET", LCD_LINE_2)
            
        elif moisture_percent < 70:
            print("Status: MOIST")
            lcd.lcd_string("Status: MOIST", LCD_LINE_2)
        else:
            print("Status: DRY")
            lcd.lcd_string("Status: DRY", LCD_LINE_2)
        
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Test ended")
    lcd.lcd_clear()
    lcd.lcd_string("Test ended", LCD_LINE_1)
    time.sleep(1)
    
finally:
    # Clean up
    lcd.lcd_clear()
    time.sleep(0.1)
