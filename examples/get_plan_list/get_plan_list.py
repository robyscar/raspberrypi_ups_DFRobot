# -*- coding:utf-8 -*-
""" 
  @file get_plan_list.py
  @brief get plan list.
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

number = ups.get_plan_len()
if number != -1:
  print("There are %d plans"%number)
time.sleep(1)

while(1):
  plan_list = plan_struct()
  '''
    # year                range (2000 to 2100)
    # month               range (1    to 12)
    # date                range (1    to 31)  # There are 29 days in February in a leap year 
    # hour                range (0    to 23)
    # minute              range (0    to 59)
    # second              range (0    to 59)
    # n_year              next alarm year
    # n_month             next alarm month
    # n_date              next alarm date
    # n_hour              next alarm hour
    # n_minute            next alarm minute
    # n_second            next alarm second
    # period_string       (/Y ,/M ,/2W ,/W ,/D) and (/1234567) 
    # types
       # AT_START_UP
       # AT_SHUTDOWN
       # AT_ALARM_START_UP
       # AT_ALARM_SHUTDOWN
    # plan_number is (1 to 20)
       # GET_PLAN_1
       # GET_PLAN_2
       # GET_PLAN_3
       # GET_PLAN_4
       # GET_PLAN_5
       # GET_PLAN_6
       # GET_PLAN_7
       # GET_PLAN_8
       # GET_PLAN_9
       # GET_PLAN_10
       # GET_PLAN_11
       # GET_PLAN_12
       # GET_PLAN_13
       # GET_PLAN_14
       # GET_PLAN_15
       # GET_PLAN_16
       # GET_PLAN_17
       # GET_PLAN_18
       # GET_PLAN_19
       # GET_PLAN_20
  '''
  plan_list = ups.get_plan_list(GET_PLAN_20)
  if plan_list.types == AT_START_UP:
    print("AT_START_UP=%d/%d/%d/%d:%d:%d%s -next alarm- %d/%d/%d/%d:%d:%d"%(plan_list.year,plan_list.month,plan_list.date,\
    plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
    plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
  elif plan_list.types == AT_SHUTDOWN:
    print("AT_SHUTDOWN=%d/%d/%d/%d:%d:%d%s -next alarm- %d/%d/%d/%d:%d:%d"%(plan_list.year,plan_list.month,plan_list.date,\
    plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
    plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
  elif plan_list.types == AT_ALARM_START_UP:
    print("AT_ALARM_START_UP=%d:%d:%d%s -next alarm- %d/%d/%d/%d:%d:%d"%(plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
    plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
  elif plan_list.types == AT_ALARM_SHUTDOWN:
    print("AT_ALARM_SHUTDOWN=%d:%d:%d%s -next alarm- %d/%d/%d/%d:%d:%d"%(plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
    plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
  else:
    print "get plan empty or error"

  '''
    # Get a list of all plans
    # number Number of plans 
  '''
  for i in range(0,number):
    plan_list = ups.get_plan_list(GET_PLAN_1+i)
    if plan_list.types == AT_START_UP:
      print("%d - AT_START_UP=%d/%d/%d/%d:%d:%d%s -next alarm- %d/%d/%d/%d:%d:%d"%(i+1,plan_list.year,plan_list.month,plan_list.date,\
      plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
      plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
    elif plan_list.types == AT_SHUTDOWN:
      print("%d - AT_SHUTDOWN=%d/%d/%d/%d:%d:%d%s -next alarm- %d/%d/%d/%d:%d:%d"%(i+1,plan_list.year,plan_list.month,plan_list.date,\
      plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
      plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
    elif plan_list.types == AT_ALARM_START_UP:
      print("%d - AT_ALARM_START_UP=%d:%d:%d%s -next alarm- %d/%d/%d/%d:%d:%d"%(i+1,plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
      plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
    elif plan_list.types == AT_ALARM_SHUTDOWN:
      print("%d - AT_ALARM_SHUTDOWN=%d:%d:%d%s -next alarm- %d/%d/%d/%d:%d:%d"%(i+1,plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
      plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
    else:
      print "get plan empty or error"
  print ""
  time.sleep(5)