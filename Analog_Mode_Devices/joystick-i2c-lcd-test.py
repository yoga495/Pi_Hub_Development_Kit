#!/usr/bin/env python3
import time
from gpiozero import MCP3008, Button
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2

# Initialize MCP3008 ADC for Joystick on channels 3, 4, and 5
# VX on channel 3, VY on channel 4, SW (button) on GPIO pin (digital)
joystick_x = MCP3008(channel=3)
joystick_y = MCP3008(channel=4)

# For the switch (SW) input, it's typically a digital input
# You would need to check which GPIO pin it's connected to
# For MCP3008 channel 5, we can use threshold to convert analog to digital
joystick_sw = MCP3008(channel=5)

# Alternative if using a direct GPIO pin for switch:
# joystick_sw = Button(pin_number, pull_up=True)

try:
    
    print("Joystick Test")
        # Initial display
    lcd.lcd_clear()
    lcd.lcd_string("***Joystick****", LCD_LINE_1)
    lcd.lcd_string("*****Test******", LCD_LINE_2)
    time.sleep(2)
    
    while True:
        # Read raw analog values (0 to 1.0)
        x_value = joystick_x.value
        y_value = joystick_y.value
        sw_pressed = joystick_sw.value
        
        # Map joystick values from 0-1 to -100 to +100
        # Typically, joysticks center at around 0.5
        x_position = int((x_value - 0.5) * 200)
        y_position = int((y_value - 0.5) * 200)
        
    
    
        print(f"X:{x_position:4d} Y:{y_position:4d}")
        lcd.lcd_clear()
        lcd.lcd_string(f"X:{x_position:4d} Y:{y_position:4d}", LCD_LINE_1)
        
        print(sw_pressed)
        # Display button state
        
        if sw_pressed == 1.0:
            print("Button: PRESSED")
            lcd.lcd_string("Button: PRESSED", LCD_LINE_2)
        else:
            print("Button: RELEASED")
            lcd.lcd_string("Button: RELEASED", LCD_LINE_2)
        
        # Add direction indicator
        
        if abs(x_position) > abs(y_position):
            # X-axis dominates   
            if x_position > 30:
                print("?")
            elif x_position < -30:
                print("?")
        else:
            # Y-axis dominates
            if y_position > 30:
                print("?")
            elif y_position < -30:
                print("?")
        
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
