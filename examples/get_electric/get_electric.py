# -*- coding:utf-8 -*-
""" 
  @file get_electric.py
  @brief Get the percentage and voltage value of the battery.
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @licence     The MIT License (MIT)
  @author      [ZhixinLiu](zhixin.liu@dfrobot.com)
  version  V1.0
  date  2021-01-27
  @get from https://www.dfrobot.com
  @url https://github.com/DFRobot/DFRobot_raspberrypi_ups
"""
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from DFRobot_raspberrypi_ups import *

I2C_MODE              = 0x01       # default use I2C1
'''
   # The first  parameter is to select i2c0 or i2c1
   # The second parameter is the i2c device address
   # The default address for i2c is I2C_ADDRESS
   # I2C_ADDRESS                    = 0x58          # i2c slave Address
'''
ups = DFRobot_raspberrypi_ups_I2C (I2C_MODE ,I2C_ADDRESS)
time.sleep(1)

while(1):
  data = ups.get_electric()
  print("voltage    = %d  mv"%data.voltage)
  print("percentage = %.2f %%\n"%data.percentage)
  time.sleep(1)