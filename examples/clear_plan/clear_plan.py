# -*- coding:utf-8 -*-
""" 
  @file clear_plan.py
  @brief clear plan.
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


# plan_number is plan number  range(0 to 20)
plan_number = ups.get_plan_len()
if plan_number != -1:
  print("There are %d plans"%plan_number)
  
'''
   # number is you want to clear the plan number
      number range is 1-20
   # return (0 is clear false) (1 is clear success)
'''
number = 1
if ups.clear_plan(number) == 1:
  print "clear success!"
else:
  print "clear false! please check plan list"

# plan_number is plan number  range(0 to 20)
plan_number = ups.get_plan_len()
if plan_number != -1:
  print("There are %d plans"%plan_number)

if ups.clear_plan_all() == 1:
  print "clear success!"
else:
  print "The list is empty! clear false!"
time.sleep(1)

while(1):
  # plan_number is plan number  range(0 to 20)
  plan_number = ups.get_plan_len()
  if plan_number != -1:
    print("There are %d plans"%plan_number)
  time.sleep(1)