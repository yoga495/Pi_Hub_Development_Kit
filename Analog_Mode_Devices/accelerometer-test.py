#!/usr/bin/env python3
import time
from gpiozero import MCP3008

# Initialize MCP3008 ADC for Accelerometer on channels 3, 4, and 5
accel_x = MCP3008(channel=3)
accel_y = MCP3008(channel=4)
accel_z = MCP3008(channel=5)

try:
 
    print("Accelerometer Sensor test")

    
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

        
        time.sleep(1)
        
except KeyboardInterrupt:
   
    print("Test ended")
    time.sleep(1)
     
finally:
    # Clean up
    time.sleep(0.1)
