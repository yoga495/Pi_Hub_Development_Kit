#!/usr/bin/env python3
import serial
import time

import pynmea2
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2


def main():
    # Initialize LCD
    lcd.lcd_clear()
    lcd.lcd_string("GPS Test", LCD_LINE_1)
    lcd.lcd_string("Initializing...", LCD_LINE_2)
    # Initial display
    time.sleep(1)
    # Configure GPS
    ser = serial.Serial('/dev/serial0', 9600, timeout=1)

    try:
        while True:
            line = ser.readline().decode('ascii', errors='replace').strip()

            # Update LCD with waiting message
            lcd.lcd_string("GPS Test", LCD_LINE_1)
            lcd.lcd_string("Waiting for fix", LCD_LINE_2)

            # Check if the message is a RMC or GGA message
            if line.startswith('$GNRMC') or line.startswith('$GPRMC') or line.startswith('$GNGGA') or line.startswith('$GPGGA'):
                try:
                    msg = pynmea2.parse(line)

                    # Check if we have latitude and longitude
                    if hasattr(msg, 'latitude') and hasattr(msg, 'longitude'):
                        lat = msg.latitude
                        lon = msg.longitude

                        # Display location on LCD (formatted to fit on 16x2 LCD)
                        lcd.lcd_string(f"Lat: {lat:.5f}", LCD_LINE_1)
                        lcd.lcd_string(f"Lon: {lon:.5f}", LCD_LINE_2)
                        

                        # Wait a bit before updating again
                        time.sleep(1)

                except Exception as e:
                    lcd.lcd_string("GPS Error", LCD_LINE_1)
                    lcd.lcd_string("Parsing data", LCD_LINE_2)
                    time.sleep(1)
                    

            time.sleep(0.1)  # Small delay to prevent CPU hogging

    except KeyboardInterrupt:
        # Clean up
        ser.close()
        lcd.lcd_byte(0x01, LCD_CMD)  # Clear display
        lcd.lcd_string("Program ended", LCD_LINE_1)
        time.sleep(1)
        time.sleep(1)
        lcd.lcd_byte(0x01, LCD_CMD)  # Clear display

if __name__ == '__main__':
    main()
