# -*- coding:utf-8 -*-
""" 
  @file set_get_time.py
  @brief set and get the time.
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

'''
   # time_struct 
   # year        range (2000 to 2100)
   # month       range (1    to 12)
   # date        range (1    to 31)  # There are 29 days in February in a leap year 
   # hour        range (0    to 23)
   # minute      range (0    to 59)
   # second      range (0    to 59)
'''
timedata = time_struct()
timedata.year   = 2021
timedata.month  = 1
timedata.date   = 29
timedata.hour   = 15
timedata.minute = 18
timedata.second = 59
if ups.set_time(timedata) == 1:
  print "set time success!"
else:
  print "set time false! please check whether the time is correct!"
time.sleep(1)

while(1):
  data = ups.get_time()              # Data contains (year ,month ,date ,hour ,minute ,second)
  print("%d/%d/%d/%d:%d:%d\n"%(data.year,data.month,data.date,data.hour,data.minute,data.second))
  time.sleep(1)