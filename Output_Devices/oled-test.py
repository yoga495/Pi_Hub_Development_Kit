import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# I2C setup
i2c = board.I2C()

# OLED display dimensions (adjust as needed)
WIDTH = 128
HEIGHT = 64

# Initialize the OLED display
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c)

# Clear the display
oled.fill(0)
oled.show()

# Create an image buffer
image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.load_default()
font = ImageFont.truetype('PixelOperator.ttf', 16)

# Demo: Hello World and other messages
try:
    while True:
            draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
            draw.text((10, 0), "Hello, User!", font=font, fill=255)
            draw.text((10, 20), "Welcome to Pi Hub", font=font, fill=255)
            draw.text((10, 40), "Development kit ", font=font, fill=255)
                                # Display image on OLED
            oled.image(image)
            oled.show()
            print("OLED print 'Hello, User! Welcome to Pi Hub Development kit'")
            
            
    
except KeyboardInterrupt:
    oled.fill(0)
    oled.show()
    print("Program ended")
