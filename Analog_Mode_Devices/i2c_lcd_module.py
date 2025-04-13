#!/usr/bin/env python3
import smbus2
import time

# LCD I2C Address
LCD_ADDRESS = 0x27  # Adjust if your LCD uses a different address

# LCD Commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

# LCD Flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# LCD Flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# LCD Flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# LCD Flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

# LCD Line Addresses
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

# I2C Expander Flags
EN = 0b00000100  # Enable bit
RW = 0b00000010  # Read/Write bit
RS = 0b00000001  # Register select bit

# Backlight flag
BACKLIGHT = 0b00001000  # Backlight bit on PCF8574

class I2CLCD:
    def __init__(self, bus=1, address=LCD_ADDRESS):
        self.bus = smbus2.SMBus(bus)
        self.address = address
        self.backlight_state = BACKLIGHT  # Backlight on by default
        self.lcd_init()

    def lcd_write(self, data, mode=0):
        """Write data to LCD with backlight state"""
        full_data = mode | (data & 0xF0) | self.backlight_state
        self.lcd_write_four_bits(full_data)
        
        full_data = mode | ((data << 4) & 0xF0) | self.backlight_state
        self.lcd_write_four_bits(full_data)

    def lcd_write_four_bits(self, data):
        """Write 4 bits to LCD"""
        self.bus.write_byte(self.address, data | EN)
        time.sleep(0.0005)
        self.bus.write_byte(self.address, ((data & ~EN)))
        time.sleep(0.0001)

    def lcd_init(self):
        """Initialize LCD with backlight on"""
        # Ensure backlight is on during initialization
        self.bus.write_byte(self.address, self.backlight_state)
        time.sleep(0.1)

        # Initialize display
        self.lcd_write(0x03)
        time.sleep(0.005)
        self.lcd_write(0x03)
        time.sleep(0.0005)
        self.lcd_write(0x03)
        time.sleep(0.0005)
        self.lcd_write(0x02)
        
        # Set LCD function
        self.lcd_write(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS, 0)
        
        # Display control
        self.lcd_write(LCD_DISPLAYCONTROL | LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF, 0)
        
        # Clear display
        self.lcd_write(LCD_CLEARDISPLAY, 0)
        time.sleep(0.002)
        
        # Entry mode set
        self.lcd_write(LCD_ENTRYMODESET | LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT, 0)

    def lcd_string(self, message, line):
        """Send string to LCD"""
        # Clear the line first
        self.lcd_write(line, 0)
        
        # Write characters
        for char in message[:16]:  # Limit to 16 characters
            self.lcd_write(ord(char), RS)

    def lcd_clear(self):
        """Clear LCD display"""
        self.lcd_write(LCD_CLEARDISPLAY, 0)
        time.sleep(0.002)

    def backlight(self, state):
        """Turn backlight on or off"""
        if state:
            self.backlight_state = BACKLIGHT
        else:
            self.backlight_state = 0x00
        # Refresh display to apply backlight state
        self.bus.write_byte(self.address, self.backlight_state)

# Global LCD object for easy import
lcd = I2CLCD()

def main():
    """Test LCD functionality"""
    try:
        print("I2C LCD Test with Backlight Control")
        
        # Clear display
        lcd.lcd_clear()
        
        # Display test messages
        lcd.lcd_string("Backlight Test", LCD_LINE_1)
        
        # Demonstrate backlight control
        print("Backlight on")
        lcd.backlight(True)
        lcd.lcd_string("Backlight: ON", LCD_LINE_2)
        time.sleep(2)
        
        print("Backlight off")
        lcd.backlight(False)
        lcd.lcd_string("Backlight: OFF", LCD_LINE_2)
        time.sleep(2)
        
        # Turn backlight back on
        print("Backlight on again")
        lcd.backlight(True)
        lcd.lcd_string("Backlight: ON", LCD_LINE_2)
        
        # Scrolling messages
        messages = [
            "Sensor Monitor",
            "I2C LCD Working",
            "Backlight Control",
            "Custom Module"
        ]
        
        while True:
            for msg in messages:
                lcd.lcd_clear()
                lcd.lcd_string(msg, LCD_LINE_1)
                time.sleep(2)
    
    except KeyboardInterrupt:
        print("LCD Test Stopped")
        lcd.lcd_clear()
        lcd.backlight(False)

if __name__ == "__main__":
    main()
