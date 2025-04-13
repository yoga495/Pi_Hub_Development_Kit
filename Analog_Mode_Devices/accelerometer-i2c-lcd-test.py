#!/usr/bin/env python3
import time
from gpiozero import MCP3008
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2

# Initialize MCP3008 ADC for Accelerometer on channels 3, 4, and 5
accel_x = MCP3008(channel=3)
accel_y = MCP3008(channel=4)
accel_z = MCP3008(channel=5)

try:
 
    print("Accelerometer Sensor test")
    lcd.lcd_clear()
    lcd.lcd_string("Accelerometer ", LCD_LINE_1)
    lcd.lcd_string("*Sensor Test**", LCD_LINE_2)
    time.sleep(1)
    
    # For scrolling display to show all three axes
    display_mode = 0
    
    while True:
        # Read raw analog values (0 to 1.0)
        x_value = accel_x.value
        y_value = accel_y.value
        z_value = accel_z.value
        
        # Map values from 0-1 to -3g to +3g (assuming a 3g accelerometer)
        # Adjust these calculations based on your accelerometer specifications
        x_g = (x_value * 6) - 3
        y_g = (y_value * 6) - 3
        z_g = (z_value * 6) - 3
        print(f"x={x_g:.2f} g y={y_g:.2f} g z= {z_g:.2f} g ")
        lcd.lcd_clear()
        lcd.lcd_string(f"x={x_g:.2f} y={y_g:.2f}", LCD_LINE_1)
        lcd.lcd_string(f"z={z_g:.2f}", LCD_LINE_2)
        time.sleep(0.5)

        
except KeyboardInterrupt:
    print("Test ended")
    lcd.lcd_clear()
    lcd.lcd_string("Test ended", LCD_LINE_1)
    time.sleep(1)
     
finally:
    # Clean up
    lcd.lcd_clear()
    time.sleep(0.1)
