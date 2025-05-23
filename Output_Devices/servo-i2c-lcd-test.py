#!/usr/bin/env python3
from gpiozero import Servo
import time
import smbus

# LCD Setup
I2C_ADDR = 0x27  # I2C device address
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1  # Mode - Sending data
LCD_CMD = 0  # Mode - Sending command

LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line

LCD_BACKLIGHT = 0x08  # On
ENABLE = 0b00000100

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

# Open I2C interface
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def lcd_init():
    # Initialise display
    lcd_byte(0x33, LCD_CMD)  # 110011 Initialize
    lcd_byte(0x32, LCD_CMD)  # 110010 Initialize
    lcd_byte(0x06, LCD_CMD)  # 000110 Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # 001100 Display On, Cursor Off, Blink Off
    lcd_byte(0x28, LCD_CMD)  # 101000 Data length, number of lines, font size
    lcd_byte(0x01, LCD_CMD)  # 000001 Clear display
    time.sleep(E_DELAY)

def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = the data
    # mode = 1 for data, 0 for command
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    # High bits
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    # Low bits
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    # Toggle enable
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)

def lcd_string(message, line):
    # Send string to display
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

def main():
    # Initialize LCD
    lcd_init()
    
    # Configure servo motor
    # Servo is connected to GPIO12
    servo = Servo(12)
    
    try:
        while True:
            # Move servo to minimum position (-1)
            lcd_string("Servo Test", LCD_LINE_1)
            lcd_string("Position: MIN", LCD_LINE_2)
            servo.min()
            time.sleep(2)
            
            # Move servo to middle position (0)
            lcd_string("Servo Test", LCD_LINE_1)
            lcd_string("Position: MID", LCD_LINE_2)
            servo.mid()
            time.sleep(2)
            
            # Move servo to maximum position (1)
            lcd_string("Servo Test", LCD_LINE_1)
            lcd_string("Position: MAX", LCD_LINE_2)
            servo.max()
            time.sleep(2)
            
    except KeyboardInterrupt:
        # Clean up
        servo.close()
        lcd_byte(0x01, LCD_CMD)  # Clear display
        lcd_string("Program ended", LCD_LINE_1)
        time.sleep(1)
        lcd_byte(0x01, LCD_CMD)  # Clear display

if __name__ == '__main__':
    main()
