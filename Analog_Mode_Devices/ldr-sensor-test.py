#!/usr/bin/env python3
import time
from gpiozero import MCP3008

# Initialize MCP3008 ADC for LDR on channel 1
ldr_sensor = MCP3008(channel=2)

def map_value(x, in_min, in_max, out_min, out_max):
    """Map value from one range to another."""
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

try:
    
    while True:
        # Read raw analog value (0 to 1.0)
        raw_value = ldr_sensor.value
        
        # Convert to percentage (0-100%)
        light_percent = int(raw_value * 100)
       
        print(f"Low Light: {light_percent}%")
        
        # Second line - visual representation
        bars = int(map_value(light_percent, 0, 100, 0, 16))
        print("=" * bars)
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("Test ended")
    time.sleep(1)
    
finally:
    # Clean up
    time.sleep(0.1)
