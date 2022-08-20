# raspberrypi_ups_DFRobot

https://wiki.dfrobot.com/ONPOWER_UPS_HAT_for_Raspberry_Pi_SKU_DFR0677
https://www.dfrobot.com/product-203.html


SKU:DFR0677
Introduction
[](Product Link)

DFRobot ONPOWER Raspberry Pi UPS hat is an uninterruptible power supply(UPS) expansion board for Raspberry Pi 3 Model B+/ 4 Model B development boards. This is a power management device specially designed for the Raspberry Pi. It can continue to supply power to the Raspberry Pi for a certain period of time in the case of an external power failure to avoid problems such as system damage and data loss caused by sudden power failure. The ONPOWER Raspberry Pi UPS hat supports USB TYPE-C power input, compatible with TYPE-C QC2.0/QC3.0, Huawei FCP and the other multiple rapid charge protocol. It can reduce the charging time while maintaining the maximum power output of 5V@3A. A 3000mAh 18650 battery can keep the system uptime for 3~4 hours, ensuring data security, but also enough to meet the needs of Raspberry Pi's daily use and mobile application scenarios. The hat has a mounting hole for DC fan, it can maintain the device running temperature. DFRobot ONPOWER Raspberry Pi UPS hat has an onboard RTC module, which we can set the time and control Raspberry Pi's power on and off via the software regularly. Cooperate with the mainboard's self-start function, it can realize timing boot/shutdown. DFRobot ONPOWER Raspberry Pi UPS expansion board uses a MAX17043 dedicated power detection chip, which is compatible with most lithium batteries on the market. The chip has its own algorithm, with the onboard LED, it can directly display the battery power capacity, and you can also get the power supply status through the serial port command.

Features
Support TYPE-C QC2.0/QC3.0, Huawei FCP and the other multiple rapid charge protocol
Maximum 5V@3A Power output
Support 18650, lithium ion, polymer lithium battery
Onboard RTC, support software timing boot/shutdown
Support LED battery capacity display and serial port information query
Specification
Input Voltage: TYPE-C QC2.0/QC3.0 Rapid charge (5V/2A; 9V/2A; 12V/1.5A)
Power Supply Interface: USB TYPE C
Battery Type: 3.7V lithium battery, 18650 lithium battery (Recommended more than 3000mAh)
Output Power: 5V@3A
Standby Power Consumption: <10mA
Communication Interface: I2C
Product Size: 65mm56mm13mm
Board Overview
Board Overview Note: Please note the battery capacity, at least 3000mAh. Higher will be better.

Tutorial
Installation Diagram
ONPOWER UPS HAT Installation Diagram
The fan can be fixed under the UPS board with M3x12 screws and M3 nuts (the side where the fan interface located)
Insert the XH2.54 2x20P long pin header from the back side (the side where the fan interface located)
Insert the female side of the row into the pin side of the Raspberry Pi, see the figure above for details.
UPS RTC(Real Time Clock) Tutorial
ONPOWER UPS HAT communicates with the Raspberry Pi through the I2C interface. We can set the time and the alarm, read the real time clock, and make timing on/off. Please download DFRobot UPS Python library, and put this folder on the desk of the Raspbian system.

Raspbian Desk

Open the I2C interface of the Raspberry Pi and enter through the terminal: sudo raspi-config

Open Raspberry Pi I2C

Select Interfacing Options-> I2C->Enable

Enable Raspberry Pi I2C

After we opened I2C interface，RTC can work now！

Change directory to DFRobot UPS Python Library Location：cd /home/pi/Desktop/DFRobot_raspberrypi_ups/python/examples/ups

Change directory

Enter Help Command, check all commands and explanations: python ups.py -p help

Enter Help Command

Help Commands

Help Commands

Examples: Synchronize the system time：python ups.py -p get_time

Synchronize the system time

There are many commands in UPS, please try more.

UPS Fan Tutorial
ONPOWER UPS HAT use BCM26(wiringPi code GPIO25；Physical pin 37) to control the fan.

Fan Driver

Sample Code

Open Thonny Python IDE, copy and paste the code, when the SoC temperature is higher than 55 degree, turn on the fan. When it is lower than 48 degree，turn off the fan.

from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) # USD BCM Pin mode

channel = 26    # BCM26(Physical pin 37)
start_temp = 55 # Startup threshold: 55(℃)
end_temp = 48   # Shutdown threshold: 48(℃)

GPIO.setup(channel, GPIO.OUT, initial = GPIO.LOW) # Initialize control pin
is_high = GPIO.LOW # GPIO Status flag

try:
    while True:
        # Get SoC temperature
        temp = open('/sys/class/thermal/thermal_zone0/temp')
        temp = int(temp.read()) / 1000

        if temp > start_temp and not is_high: # When the SoC temperature exceeds the startup threshold and the fan is off
            GPIO.output(channel, GPIO.HIGH)   # Turn on the fan
            is_high = GPIO.HIGH               # Mark the fan status as on

        elif temp < end_temp and is_high:     # When the SoC temperature is below the shutdown threshold and the fan is on
            GPIO.output(channel, GPIO.LOW)    # Turn off the fan
            is_high = GPIO.LOW                # Mark the fan status as off

        sleep(10) # 10s
except:
    pass
# Reset this pin when exiting
GPIO.cleanup(channel)



https://www.dfrobot.com/product-203.html
Gravity: Terminal Sensor Adapter V2.0
Gravity: Terminal Sensor Adapter V2.0
Screw Shield for Arduino
Screw Shield for Arduino

$7.50

Screw Terminal 3.5mm Pitch(2-Pin)
Screw Terminal 3.5mm Pitch(2-Pin)

$0.69

Gravity: Screw Shield V2 for Arduino
Gravity: Screw Shield V2 for Arduino

$7.50

Waterproof DS18B20 Digital Temperature Sensor for Arduino
Waterproof DS18B20 Digital Temperature Sensor for Arduino

$6.90

Screwless Terminal Shield For Arduino
Screwless Terminal Shield For Arduino

$9.50

Gravity: Analog Adjustable Infrared Sensor Switch (50cm)
Gravity: Analog Adjustable Infrared Sensor Switch (50cm)

$6.80

Gravity: Waterproof DS18B20 Sensor Kit
Gravity: Waterproof DS18B20 Sensor Kit

$7.50

Magnetic Contact Switch Sensor for Arduino
Magnetic Contact Switch Sensor for Arduino

$4.00

Waterproof SMD DS18B20 Digital Temperature Sensor
Waterproof SMD DS18B20 Digital Temperature Sensor

$6.90

You have choosen:0

Total amount: $0
BUY IT NOW
INTRODUCTION
This is  universal sensor adapter V2.0, it can be accessed by digital input modules and analog input module. The module with Arduino sensor expansion board, in combination.Improvment compare with the old version,we add a 10K resistor between A & B, A & C respectively,so that you  needn't to connect a addition resistor while the sensor must have a pull-up or pull-down resistor. Why need a pull-up or pull down resistor, please refer to"Understanding pull-up and pull-down resistors"
Generally speaking, this terminal provides a much easier way to connect a switch or any modules that requires pull-up/down resistor to microcontroller .
SPECIFICATION
Voltage: +5 V
Current: <1000mA
Size: 22x34mm (0.87x1.3 in)
https://www.dfrobot.com/wiki/index.php/Terminal_sensor_adapter_V2_SKU:DFR0055
https://image.dfrobot.com/image/data/DFR0055/V2.0/Terminal%20sensor%20adapter%20V2%20SCH.pdf

