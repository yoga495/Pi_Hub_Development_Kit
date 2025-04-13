# Raspberry Pi Analog Device Sensor Suite

This repository contains Python scripts for testing and monitoring various analog sensors connected to a Raspberry Pi through an MCP3008 Analog-to-Digital Converter (ADC) and displaying the results on an I2C LCD display.

## Project Overview

This project provides test scripts for the following analog sensors:
- LDR (Light Dependent Resistor)
- Soil Moisture Sensor
- Turbidity Sensor
- Voltage Sensor
- 3-Axis Accelerometer
- Joystick

All sensors connect to the Raspberry Pi through an MCP3008 ADC, and readings are displayed on an I2C LCD (connected to GPIO2/SDA and GPIO3/SCL).

## Hardware Requirements

- Raspberry Pi (any model with GPIO pins)
- MCP3008 Analog-to-Digital Converter
- I2C LCD Display (16x2 with PCF8574 I2C backpack)
- Various analog sensors:
  - LDR (Light Dependent Resistor)
  - Soil Moisture Sensor
  - Turbidity Sensor
  - Voltage Sensor
  - 3-Axis Accelerometer
  - Joystick

## Connection Details

### MCP3008 to Raspberry Pi
- VDD → 3.3V
- VREF → 3.3V
- AGND → GND
- CLK → GPIO11 (SCLK)
- DOUT → GPIO9 (MISO)
- DIN → GPIO10 (MOSI)
- CS → GPIO8 (CE0)
- DGND → GND

### I2C LCD to Raspberry Pi
- VCC → 5V
- GND → GND
- SDA → GPIO2
- SCL → GPIO3

### Sensor Connections to MCP3008

| Sensor | Description | From JST Connector | To JST Connector | Sensor pin to MCP3008 Channel |
|--------|-------------|------------------|-----------------|------------------------------|
| LDR | Light sensor | U10 | U23 | A0 pin to CH1 |
| Moisture | Soil moisture | U9 | U22 | A0 pin to CH0 |
| Turbidity | Fluid cloudiness | U11 | U24 | A0 pin to CH2 |
| Voltage | Voltage Monitoring | U28 | U26 | OUT pin to CH6 |
| Accelerometer | Motion/orientation | U20 | CN2 | X0,Y0,Z0 to CH3,CH4,CH5 |
| Joystick | Position control | CN8 | CN2 | VX,VY,SW to CH3,CH4,CH5 |

## Software Requirements

- Python 3
- Required Python packages:
  - gpiozero
  - RPLCD
  - smbus2 (for I2C)

## Installation

1. Install required packages:
```bash
sudo apt-get update
sudo apt-get install python3-pip python3-smbus i2c-tools
sudo pip3 install gpiozero RPLCD
```

2. Enable SPI and I2C interfaces on your Raspberry Pi:
```bash
sudo raspi-config
```
Navigate to "Interface Options" and enable both SPI and I2C.

3. Clone this repository:
```bash
git clone https://github.com/yoga495/Pi_Hub_Development_kit.git
cd rpi-analog-sensors
```

4. Make the scripts executable:
```bash
chmod +x *.py
```

## Usage


### Testing the MCP3008 ADC

Test all channels:
```bash
python3 mcp3008-test.py
```

### Testing Individual Sensors

#### LDR (Light Sensor)
```bash
python3 ldr-sensor-test.py
```

#### Soil Moisture Sensor
```bash
python3 moisture-sensor-test.py
```

#### Turbidity Sensor
```bash
python3 turbidity-sensor-test.py
```

#### pH Sensor
```bash
python3 voltage-sensor-test.py
```

#### Accelerometer
```bash
python3 accelerometer-test.py
```

#### Joystick
```bash
python3 joystick-test.py
```


## Calibration

Most analog sensors require calibration for accurate readings. Default calibration values are provided in the scripts, but you should adjust these based on your specific sensors:

- For the moisture sensor, measure values in both dry air and water.
- For the turbidity sensor, use clean water and a standard turbidity solution.

## Troubleshooting

### LCD Display Issues
- Check the I2C address (default is 0x27, but some displays use 0x3F)
- Run `i2cdetect -y 1` to find the correct address

### Sensor Reading Issues
- Verify the MCP3008 connections
- Check that you're connected to the correct JST port
- Ensure the sensor is powered correctly

## Script Descriptions

- `mcp3008-lcd-common.py`: Common functions for MCP3008 and I2C LCD
- `lcd-test.py`: Test script for I2C LCD display
- `mcp3008-test.py`: Test script for MCP3008 ADC
- `ldr-sensor-test.py`: Test script for LDR light sensor
- `moisture-sensor-test.py`: Test script for soil moisture sensor
- `turbidity-sensor-test.py`: Test script for turbidity sensor
- `voltage-sensor-test.py`: Test script for voltage sensor
- `accelerometer-test.py`: Test script for accelerometer
- `joystick-test.py`: Test script for joystick

## License

This project is released under the MIT License.
