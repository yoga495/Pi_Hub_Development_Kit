# Raspberry Pi Input Device Sensor Test Suite

This repository contains test scripts for various sensors connected to a Raspberry Pi via GPIO pins as specified in the connection table. Each script tests an individual sensor and displays the data on an I2C LCD display.

## Hardware Requirements

- Raspberry Pi 4 
- DHT11
- PIR
- Ultrasonic
- BMP
- Gyroscope
- BP Sensor
- Switch (Push Buttons)
- GPS

## Connection Table

| S.no | Sensor | Description | Pinout Description | From JST Connector No. | To JST Connector No | Sensor pin connected to Raspberry Pi GPIO |
|------|--------|-------------|-------------------|------------------------|---------------------|------------------------------------------|
| 1 | DHT11 | Measures temperature and humidity | VCC, GND, Data | U13 | U2 | Data pin to GPIO 17 |
| 2 | PIR | Detects motion by sensing changes in infrared radiation | VCC, GND, Out | U14 | U1 | Out pin to GPIO4 |
| 3 | Ultrasonic | Measures distance using ultrasonic sound waves | VCC, GND, Trig, Echo | U16 | U4 | Trig pin to GPIO5, Echo pin to GPIO 6 |
| 4 | BMP | Measures barometric pressure and temperature | VCC, GND, SCL, SDA | U21 | U5 | SCL pin to GPIO3, SDA pin to GPIO2 |
| 5 | Gyroscope | Measures angular velocity or rotational rate | VCC, GND, SCL, SDA | CN1 | U66 | SCL pin to GPIO3, SDA pin to GPIO2 |
| 6 | BP Sensor | Measures blood pressure | VCC, SDA, SCL, GND | U44 | U66 | SCL pin to GPIO3, SDA pin to GPIO2 |
| 7 | Switch | Detects a closed or open circuit, indicating an on/off state | VCC, GND, SW1, SW2 | U25 | U34 | SW1 to GPIO22, SW2 to GPIO27 |
| 8 | GPS | Location via satellite | VCC, GND, RX, TX | U19 | U6 | RX->UART_TX, TX->UART_RX |

## LCD Display Connection
The I2C LCD display is connected to:
- SCL pin to GPIO3
- SDA pin to GPIO2


## Test Scripts
 Clone this repository:
```bash
git clone https://github.com/yoga495/Pi_Hub_Development_Kit.git
cd Input_Devices
```
### Individual Sensor Tests

Each sensor has its own dedicated test script:


1. `dht11-sensor-test.py` - Tests the DHT11 temperature and humidity sensor
2. `pir-motion-sensor-test.py` - Tests the PIR motion detection sensor
3. `ultrasonic-sensor-test.py` - Tests the ultrasonic distance sensor
4. `bmp-pressure-sensor-test.py` - Tests the BMP barometric pressure sensor
5. `gyroscope-sensor-test.py` - Tests the gyroscope sensor
6. `bp-sensor-test.py` - Tests the blood pressure sensor
7. `switch-test.py` - Tests the switch sensor
8. `gps-test.py` - Tests just the I2C LCD display

### Integrated Test

The `all_sensors_test.py` script tests all sensors simultaneously using threading. It cycles through displaying data from each sensor on the LCD display.

## Running the Tests

Make each script executable and run it:

```bash
chmod +x <script_name>.py
./<script_name>.py
```

For example:
```bash
chmod +x dht11-sensor-test.py
./dht11-sensor-test.py
```

## Troubleshooting

If you encounter issues:

1. Check all connections according to the connection table
2. Verify that I2C and UART interfaces are enabled:
   ```bash
   sudo raspi-config
   ```
   Navigate to "Interface Options" and enable I2C and Serial

3. Check if I2C devices are detected:
   ```bash
   sudo i2cdetect -y 1
   ```

4. Ensure proper power supply to all sensors

5. Check that all required libraries are installed:
   ```bash
   pip install gpiozero Adafruit_DHT adafruit_blinka adafruit_circuitpython_mpu6050 pyserial smbus2
   ```

## Notes

- The BP,BMP and Gyroscope sensors both use I2C and share the same GPIO pins (GPIO2 for SDA and GPIO3 for SCL)
- The LCD display also uses I2C on the same GPIO pins as the BMP and Gyroscope
- Make sure to connect GND and VCC for all sensors appropriately
- Adjust I2C address in i2c_lcd_module.py if needed (common addresses are 0x27 or 0x3F)
- Some sensors (BMP, Gyroscope) use I2C, so they share the same I2C bus
- Each script is self-contained and can be run independently

## Additional Resources

- GPIO Zero documentation: https://gpiozero.readthedocs.io/
- Adafruit CircuitPython libraries: https://circuitpython.readthedocs.io/
- RPLCD documentation: https://rplcd.readthedocs.io/
