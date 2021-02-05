# -*- coding:utf-8 -*-
""" 
  @file set alarm.py
  @brief set alarm.
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
nowtime=time_struct()
nowtime.year   = 2021
nowtime.month  = 1
nowtime.date   = 29
nowtime.hour   = 13
nowtime.minute = 40
nowtime.second = 0
if ups.set_time(nowtime) == 1:
  print "set time success!"
else:
  print "set time false! please check whether the time is correct!"

'''
   # time_struct 
   # year        range (2000 to 2100)
   # month       range (1    to 12)
   # date        range (1    to 31)  # There are 29 days in February in a leap year 
   # hour        range (0    to 23)
   # minute      range (0    to 59)
   # second      range (0    to 59)
   # types is 
       SET_ONE_STARTING_UP         Set a boot time 
       SET_ONE_SHUTDOWN            Set a shutdown time 
       SET_YEAR_STARTING_UP        Set up an annual cycle start 
       SET_YEAR_SHUTDOWN           Set the shutdown cycle in years 
       SET_MONTH_STARTING_UP       Set up a monthly cycle 
       SET_MONTH_SHUTDOWN          Set a monthly shutdown 
       SET_TWO_WEEK_STARTING_UP    Set up a two-week cycle boot 
       SET_TWO_WEEK_SHUTDOWN       Set a two-week cycle shutdown 
       SET_WEEK_STARTING_UP        Set a weekly boot 
       SET_WEEK_SHUTDOWN           Set a weekly shutdown 
       SET_DATE_STARTING_UP        Set a day-cycle boot 
       SET_DATE_SHUTDOWN           Set the shutdown cycle in days 
'''
timedata = time_struct()
timedata.year   = 2021
timedata.month  = 1
timedata.date   = 29
timedata.hour   = 13
timedata.minute = 40
timedata.second = 25
timedata.types  = SET_DATE_SHUTDOWN
if ups.set_at_time(timedata) != 1:
  print "Please check whether the time is correct!"


timedata.year   = 2021
timedata.month  = 1
timedata.date   = 29
timedata.hour   = 13
timedata.minute = 40
timedata.second = 35
timedata.types  = SET_ONE_STARTING_UP
if ups.set_at_time(timedata) != 1:
  print "Please check whether the time is correct!"

'''
   # alarm_time_struct 
   # hour        range (0 to 23)
   # minute      range (0 to 59)
   # second      range (0 to 59)
   # types is 
      SET_ONE_ALARM_STARTING_UP = 0x0f      Set an Alarm ,Don't need a period
      SET_ONE_ALARM_SHUTDOWN    = 0x10      Set an Alarm ,Don't need a period

      SET_ALARM_STARTING_UP     = 0x11      set the loop alarm, need a period
      SET_ALARM_SHUTDOWN        = 0x12      set the loop alarm, need a period
   # period is cycle week
       ________________________________________________________________________
      |reserve |sunday |saturday |Friday |Thursday |Wednesday |Tuesday |Monday |
      |0       |0      |0        |0      |0        |0         |0       |0      |
      |________|_______|_________|_______|_________|__________|________|_______|
      eg: 0b00000001 is monday
          0b00100001 is saturday ,monday
          0b01111111 is sunday ,saturday ,Friday ,Thursday ,Wednesday ,Tuesday ,Monday
'''
alarmdata = alarm_time_struct()
alarmdata.hour   = 13
alarmdata.minute = 40
alarmdata.second = 42
alarmdata.types  = SET_ONE_ALARM_SHUTDOWN
if ups.set_alarm_time(alarmdata) != 1:
  print "Please check whether the time is correct!"


alarmdata.hour   = 13
alarmdata.minute = 40
alarmdata.second = 50
alarmdata.types  = SET_ALARM_STARTING_UP
alarmdata.period = 0b00001111

if ups.set_alarm_time(alarmdata) != 1:
  print "Please check whether the time is correct!"
time.sleep(1)

while(1):
  data = ups.get_time()
  print("%d/%d/%d/%d:%d:%d\n"%(data.year,data.month,data.date,data.hour,data.minute,data.second))
  time.sleep(1)