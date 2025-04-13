#!/usr/bin/env python3
import time
import board
import adafruit_dht
import busio
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2

# Define DHT11 sensor
dht_pin = board.D17 # GPIO17
dht_sensor = adafruit_dht.DHT11(dht_pin)

def main():
    try:
        print("DHT11 Sensor Test. Press CTRL+C to exit")
        
        # Initial display
        lcd.lcd_clear()
        lcd.lcd_string("DHT11 Sensor", LCD_LINE_1)
        lcd.lcd_string("Temperature Test", LCD_LINE_2)
        time.sleep(2)
        
        while True:
              # Read Temperature & Humidity
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity
            
            if humidity is not None and temperature is not None:
                print(f"Temperature: {temperature:.1f}'C, Humidity: {humidity:.1f}%")
                
                # Display on LCD - split across two lines
                lcd.lcd_clear()
                lcd.lcd_string(f"Temp: {temperature:.1f}'C", LCD_LINE_1)
                lcd.lcd_string(f"Humidity: {humidity:.1f}%", LCD_LINE_2)
            else:
                print("Failed to retrieve data from DHT11 sensor")
                lcd.lcd_clear()
                lcd.lcd_string("Sensor Error!", LCD_LINE_1)
                lcd.lcd_string("Check Connection", LCD_LINE_2)
            
            # Wait before next reading
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("Program stopped")
    finally:
        lcd.lcd_clear()

if __name__ == "__main__":
    main()
