#!/usr/bin/env python3
import serial
import time
import smbus
import pynmea2


def main():

    # Configure GPS
    ser = serial.Serial('/dev/serial0', 9600, timeout=1)

    try:
        while True:
            line = ser.readline().decode('ascii', errors='replace').strip()


            # Check if the message is a RMC or GGA message
            if line.startswith('$GNRMC') or line.startswith('$GPRMC') or line.startswith('$GNGGA') or line.startswith('$GPGGA'):
                try:
                    msg = pynmea2.parse(line)

                    # Check if we have latitude and longitude
                    if hasattr(msg, 'latitude') and hasattr(msg, 'longitude'):
                        lat = msg.latitude
                        lon = msg.longitude


                        print(f"Lat: {lat:.5f}")
                        print(f"Lon: {lon:.5f}")

                        # Wait a bit before updating again
                        time.sleep(1)

                except Exception as e:
                    time.sleep(1)
                    print ("GPS Error Parsing data")

            time.sleep(0.1)  # Small delay to prevent CPU hogging

    except KeyboardInterrupt:
        # Clean up
        ser.close()

        print("Program ended")
        time.sleep(1)


if __name__ == '__main__':
    main()
