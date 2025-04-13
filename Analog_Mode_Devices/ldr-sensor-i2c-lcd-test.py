#!/usr/bin/env python3
import time
from gpiozero import MCP3008
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2

# Initialize MCP3008 ADC for LDR on channel 1
ldr_sensor = MCP3008(channel=1)

def map_value(x, in_min, in_max, out_min, out_max):
    """Map value from one range to another."""
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

try:
    print("LDR Sensor Test. Press CTRL+C to exit")
    # Initial display
    lcd.lcd_clear()
    lcd.lcd_string("LDR Sensor Test", LCD_LINE_1)
    lcd.lcd_string("***************", LCD_LINE_2)
    time.sleep(2)
    while True:
        # Read raw analog value (0 to 1.0)
        raw_value = ldr_sensor.value
        
        # Convert to percentage (0-100%)
        light_percent = int(raw_value * 100)
        # Second line - visual representation
        bars = int(map_value(light_percent, 0, 100, 0, 16))
        print("=" * bars)
        time.sleep(0.5)
        
        print(f"Low Light: {light_percent}%")
        lcd.lcd_clear()
        lcd.lcd_string(f"Low Light: {light_percent}%", LCD_LINE_1)
        lcd.lcd_string("=" * bars, LCD_LINE_2)
        time.sleep(0.1)
        
        
        
except KeyboardInterrupt:
    print("Test ended")
    lcd.lcd_clear()
    lcd.lcd_string("Test ended", LCD_LINE_1)
    time.sleep(1)

    
finally:
    # Clean up
    lcd.lcd_clear()
    time.sleep(0.1)
