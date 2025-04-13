#!/usr/bin/env python3
import time
import bmpsensor




def main():
    try:
        print("BMP Pressure Sensor Test. Press CTRL+C to exit")
        
        while True:
            temperature, pressure, altitude = bmpsensor.readBmp180()
            
            # Print to terminal
            print(f"Temperature: {temperature:.1f}'C")
            print(f"Pressure: {pressure:.1f} hPa")
            print(f"Altitude: {altitude:.1f} meters")
            print("------------------------")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("Program stopped")
    finally:
        time.sleep(1)

if __name__ == "__main__":
    main()
