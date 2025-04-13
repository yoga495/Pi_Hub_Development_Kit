import max30102
import hrcalc
import time
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2

# Initialize the MAX30102 sensor
m = max30102.MAX30102()

def read_sensor():
    try:
        while True:
            # Read data from the sensor
            red, ir = m.read_sequential()
            # Calculate heart rate and SpO2
            hr, hr_valid, spo2, spo2_valid = hrcalc.calc_hr_and_spo2(ir, red)

            # Check if valid readings are obtained
            if hr_valid and spo2_valid:
                print("Heart Rate: ", hr, "BPM")
                print("SpO2 Level: ", spo2, "%")
                # Display on LCD
                lcd.lcd_clear()
                lcd.lcd_string(f"HR: {hr} BPM", LCD_LINE_1)
                lcd.lcd_string(f"SpO2: {spo2}%", LCD_LINE_2)
                
                # Wait before next reading
                time.sleep(0.1)
            else:
                print("Invalid readings. Please try again.")
                lcd.lcd_clear()
                lcd.lcd_string("Invalid readings.", LCD_LINE_1)
                lcd.lcd_string("Please try again.", LCD_LINE_2)

            # Wait for a short time before reading again
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("Program stopped")
    finally:
        lcd.lcd_clear()

if __name__ == "__main__":
    read_sensor()
