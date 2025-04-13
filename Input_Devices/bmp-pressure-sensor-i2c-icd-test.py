#!/usr/bin/env python3
import time
import bmpsensor
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2



def main():
    try:
        print("BMP Pressure Sensor Test. Press CTRL+C to exit")
        
        # Initial display
        lcd.lcd_clear()
        lcd.lcd_string("BMP Pressure", LCD_LINE_1)
        lcd.lcd_string("Sensor Test", LCD_LINE_2)
        time.sleep(2)
        
        while True:
            temperature, pressure, altitude = bmpsensor.readBmp180()
            
            # Print to terminal
            print(f"Temperature: {temperature:.1f}'C")
            print(f"Pressure: {pressure:.1f} hPa")
            print(f"Altitude: {altitude:.1f} meters")
            print("------------------------")
            
            # Cycle through display modes
            display_modes = [
                (f"Temp: {temperature:.1f}C", ""),
                (f"Press: {pressure:.1f}", "hPa"),
                (f"Alt: {altitude:.1f}", "meters")
            ]
            
            for mode in display_modes:
                lcd.lcd_clear()
                lcd.lcd_string(mode[0], LCD_LINE_1)
                lcd.lcd_string(mode[1], LCD_LINE_2)
                time.sleep(2)
            
    except KeyboardInterrupt:
        print("Program stopped")
    finally:
        lcd.lcd_clear()

if __name__ == "__main__":
    main()
