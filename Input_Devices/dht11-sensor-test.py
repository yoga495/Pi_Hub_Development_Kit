import time
import board
import adafruit_dht
import busio


# Define DHT11 sensor
dht_pin = board.D17 # GPIO17
dht_sensor = adafruit_dht.DHT11(dht_pin)

try:
    while True:
        try:
            # Read Temperature & Humidity
            temp = dht_sensor.temperature
            humidity = dht_sensor.humidity

            if temp is not None and humidity is not None:
                # Print to terminal
                print(f"Temp: {temp:.1f}'C, Humidity: {humidity:.1f}%")
            else:
                print("Failed to get reading. Retrying...")

        except RuntimeError as e:
            print(f"Reading error: {e}")
        
        time.sleep(2)  # Wait 2 seconds before next reading

except KeyboardInterrupt:
    print("\nScript stopped by user.")
    dht_sensor.exit()
