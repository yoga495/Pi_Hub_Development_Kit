#!/usr/bin/env python3
import time
from gpiozero import MCP3008

# Initialize MCP3008 ADC for Turbidity sensor on channel 2
turbidity_sensor = MCP3008(channel=2)

# Calibration values - adjust these based on your sensor and measurements
CLEAR_WATER = 0.57 # Value for clear water
UNTRETED_WATER = 0.3  # Value for very turbid water

try:
    print("Turbidity Sensor Test. Press CTRL+C to exit")    
    while True:
        # Read raw analog value (0 to 1.0)
        raw_value = turbidity_sensor.value
        #print(f"rawvalue:{raw_value}")
        # Convert to NTU (Nephelometric Turbidity Units) - simplified calculation
        # Proper conversion depends on sensor calibration based on the raw value 
        if raw_value >= CLEAR_WATER:
            ntu = 0
        elif raw_value <= UNTRETED_WATER:
            ntu = 3000  # Highly turbid
        else:
            # Linear mapping between calibration points
            ntu = int((CLEAR_WATER - raw_value) / (CLEAR_WATER - UNTRETED_WATER) * 3000)
        
        # Display on LCD
        
        print(f"Turbidity: {ntu} NTU")
        
        
        # Display water quality
        
        if ntu < 5:
            print("Quality: CLEAR")
        elif ntu < 500:
            print("Quality: CLOUDY")
        else:
            print("Quality: UNTRETED")
        
        time.sleep(1)
        
except KeyboardInterrupt:
    
    print("Test ended")
    time.sleep(1)
    
    
finally:
    # Clean up
    time.sleep(1)
