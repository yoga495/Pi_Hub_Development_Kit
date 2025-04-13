# Raspberry Pi Output Device Test Scripts

This repository contains test scripts for various output devices connected to a Raspberry Pi using JST connectors. Each script tests a specific device and displays the device status on a 16x2 I2C LCD display.

## Table of Contents
1. [Hardware Requirements](#hardware-requirements)
2. [Software Requirements](#software-requirements)
3. [Connection Details](#connection-details)
4. [Setup Instructions](#setup-instructions)
5. [Individual Test Scripts](#individual-test-scripts)
6. [Troubleshooting](#troubleshooting)

## Hardware Requirements
- Raspberry Pi (any recent model with 40-pin GPIO header)
- I2C 16x2 LCD Display (connected to SCL:GPIO3, SDA:GPIO2)
- LED (connected to GPIO18, GPIO16)
- RGB LED (connected to GPIO26:Blue, GPIO19:Green, GPIO13:Red)
- Servo Motor (connected to GPIO12)
- Buzzer (connected to GPIO25)
- OLED Display (connected to SCL:GPIO3, SDA:GPIO2)
- 2-Channel Relay Module (connected to GPIO24, GPIO23)
  

## Software Requirements
Before running the scripts, install the following dependencies:

```bash
# Update package lists
sudo apt-get update

# Install I2C tools
sudo apt-get install -y python3-smbus i2c-tools

# Install GPIO Zero library
sudo apt-get install -y python3-gpiozero

# Install other required packages
sudo pip3 install adafruit-circuitpython-ssd1306
sudo pip3 install pynmea2
sudo pip3 install pillow
sudo pip3 install pyserial
```

## Connection Details
The devices are connected via JST connectors as follows:

| Output Device | Description | Pinout | From JST | To JST | RPi GPIO |
|---------------|-------------|--------|----------|--------|----------|
| LED | Light emitting diode | VCC, GND, LED1, LED2 | U12 | U18 | LED1->GPIO18, LED2->GPIO16 |
| RGB LED | SMD5050 RGB LED | R, G, B, GND | U3 | U15 | B->GPIO26, G->GPIO19, R->GPIO13 |
| Servo Motor | Position-specific motor | VCC, GND, SIG | U32 | U35 | SIG->GPIO12 |
| BUZZER | Sound producer | VCC, SIG | CN6 | CN7 | SIG->GPIO25 |
| OLED | Organic LED display | VCC, GND, SCL, SDA | U69 | U67 | SCL->GPIO3, SDA->GPIO2 |
| Relay | 2ch 5V relay module | VCC, GND, IN1, IN2 | U30 | U31 | IN2->GPIO24, IN1->GPIO23 |
| 16x2 LCD | Character display | VCC, GND, SCL, SDA | U17 | U67 | SCL->GPIO3, SDA->GPIO2 |

## Setup Instructions

### Enable I2C Interface
1. Run `sudo raspi-config`
2. Navigate to 'Interfacing Options'
3. Select 'I2C' and enable it
4. Also enable 'Serial' for GPS module (but disable serial console)
5. Reboot your Raspberry Pi

### Enable Serial Interface (for GPS)
1. Run `sudo raspi-config`
2. Navigate to 'Interfacing Options'
3. Select 'Serial'
4. Disable login shell over serial
5. Enable serial hardware
6. Reboot your Raspberry Pi

### Verify I2C Devices
```bash
# Scan for I2C devices
sudo i2cdetect -y 1
```
You should see addresses for your LCD (typically 0x27) and OLED display (typically 0x3C).

## Individual Test Scripts
### Clone this repository:
```bash
git clone https://github.com/yoga495/Pi_Hub_Development_Kit.git
cd Output_Devices
```
### 1. LED Test (`led-test.py`)
Tests two LEDs connected to GPIO18 and GPIO16.
```bash
sudo python3 led-test.py
```

### 2. RGB LED Test (`rgb-led-test.py`)
Tests an RGB LED connected to GPIO26 (Blue), GPIO19 (Green), GPIO13 (Red).
```bash
sudo python3 rgb-led-test.py
```

### 3. Servo Motor Test (`servo-test.py`)
Tests a servo motor connected to GPIO12.
```bash
sudo python3 servo-test.py
```

### 4. Buzzer Test (`buzzer-test.py`)
Tests a buzzer connected to GPIO25.
```bash
sudo python3 buzzer-test.py
```

### 5. OLED Display Test (`oled-test.py`)
Tests an OLED display connected to I2C (GPIO3/GPIO2).
```bash
sudo python3 oled-test.py
```

### 6. Relay Test (`relay-test.py`)
Tests a 2-channel relay module connected to GPIO24 and GPIO23.
```bash
sudo python3 relay-test.py
```

### 7. 16x2 LCD Test (`lcd-test.py`)
Tests a 16x2 LCD display connected to I2C (GPIO3/GPIO2).
```bash
sudo python3 lcd-test.py
```

## Execution Details
Each script follows this general pattern:
1. Initialize the 16x2 LCD display
2. Configure the specific output device
3. Run a test sequence demonstrating the device functionality
4. Display the device status on the LCD
5. Clean up on program termination (Ctrl+C)

All scripts require sudo permissions to access GPIO pins:
```bash
sudo python3 script-name.py
```

## Troubleshooting
-It looks like you're encountering an "externally-managed-environment"
error when trying to install Python packages with pip. This error occurs 
in newer versions of Raspberry Pi OS (and other recent Debian/Ubuntu distributions) 
that use a Python virtual environment system to maintain system stability.
Here are a few ways to solve this issue:

### Option 1: Use apt to install packages (preferred for system stability)
```bash
sudo apt-get update
sudo apt-get install python3-adafruit-circuitpython-ssd1306
```
### Option 2: Use pip with the --break-system-packages flag (use with caution)
```bash
sudo pip3 install --break-system-packages adafruit-circuitpython-ssd1306
```
### Option 3: Create a virtual environment (recommended for development)
# Install venv package
```bash
sudo apt-get install python3-venv

# Create a virtual environment
python3 -m venv ~/output_device_env

# Activate the virtual environment
source ~/output_device_env/bin/activate

# Install packages within the virtual environment
pip3 install adafruit-circuitpython-ssd1306 pillow pyserial gpiozero smbus2
```
When using Option 3, you'll need to activate the virtual environment before running
your scripts, or update your scripts' shebang line to point to the virtual 
environment's Python interpreter.

### I2C Issues
- If LCD/OLED is not detected, check the I2C address with `sudo i2cdetect -y 1`
- Verify your connections (SCL to GPIO3, SDA to GPIO2)
- Check that I2C is enabled in raspi-config

### GPIO Issues
- Ensure you're running the scripts with sudo permissions
- Verify the GPIO pin numbers in the script match your connections
- Check for proper grounding of devices

### GPS Issues
- Make sure serial console is disabled but serial hardware is enabled
- Check UART connections (GPS TX to RPi RX, GPS RX to RPi TX)
- GPS may need time to acquire a satellite fix when outdoors

### Permissions Issues
If you get permissions errors:
```bash
# Make scripts executable
chmod +x *.py

# Run with sudo
sudo ./script-name.py
```

For additional help or to report issues, please post your comments here:
https://www.hackster.io/yoganandham2012/pi-hub-development-kit-a-versatile-modular-iot-prototyping-ca311e.
