#!/usr/bin/env python3
import time
import board
import adafruit_mpu6050
from i2c_lcd_module import lcd, LCD_LINE_1, LCD_LINE_2

# MPU6050 Gyroscope setup - using I2C
i2c = board.I2C()  # uses board.SCL (GPIO3) and board.SDA (GPIO2)
mpu = adafruit_mpu6050.MPU6050(i2c)

def main():
    try:
        print("Gyroscope Sensor Test. Press CTRL+C to exit")
        
        # Initial display
        lcd.lcd_clear()
        lcd.lcd_string("Gyroscope", LCD_LINE_1)
        lcd.lcd_string("Sensor Test", LCD_LINE_2)
        time.sleep(2)
        
        while True:
            # Read gyroscope data
            gyro = mpu.gyro
            accel = mpu.acceleration
            temp = mpu.temperature
            
            # Print to terminal
            print(f"Gyro X: {gyro[0]:.2f}, Y: {gyro[1]:.2f}, Z: {gyro[2]:.2f} rad/s")
            print(f"Accel X: {accel[0]:.2f}, Y: {accel[1]:.2f}, Z: {accel[2]:.2f} m/s^2")
            print(f"Temperature: {temp:.1f}'C")
            print("------------------------")
            
            # Cycle through display modes
            display_modes = [
                (f"Gyro X: {gyro[0]:.1f}", f"Gyro Y: {gyro[1]:.1f}"),
                (f"Accel X: {accel[0]:.1f}", f"Accel Y: {accel[1]:.1f}"),
                (f"Temp: {temp:.1f}C", f"Z-Accel: {accel[2]:.1f}")
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
