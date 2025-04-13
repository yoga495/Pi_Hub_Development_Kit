#!/usr/bin/env python3
import time
from gpiozero import MCP3008

# Initialize MCP3008 ADC for Moisture sensor on channel 0
moisture_sensor = MCP3008(channel=0)

# Calibration values - adjust these based on your sensor and soil type
# These values need to be calibrated for your specific soil and sensor
DRY_VALUE = 0.8  # Value when sensor is in dry air
WET_VALUE = 0.2  # Value when sensor is in water

try:
    print("Moisture Sensor Test. Press CTRL+C to exit")
    
    while True:
        # Read raw analog value (0 to 1.0)
        raw_value = moisture_sensor.value
        print(moisture_sensor.value)
        # Convert to percentage (0% = dry, 100% = wet)
        if raw_value >= DRY_VALUE:
            moisture_percent = 100
        elif raw_value <= WET_VALUE:
            moisture_percent = 0
        else:
            moisture_percent = int((DRY_VALUE - raw_value) / (DRY_VALUE - WET_VALUE) * 100)
        

        print(f"Moisture: {moisture_percent}%")
        
        # Display status message
        
        if moisture_percent < 30:
            print("Status: WET")
        elif moisture_percent < 70:
            print("Status: MOIST")
        else:
            print("Status: DRY")
        
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Test ended")
    time.sleep(0.1)
    
finally:
    # Clean up
    time.sleep(0.1)
