# -*- coding: utf-8 -*
""" 
  @file DFRobot_raspberrypi_ups.py
  @note DFRobot_raspberrypi_ups Class infrastructure, implementation of underlying methods
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @licence     The MIT License (MIT)
  @author      [ZhixinLiu](zhixin.liu@dfrobot.com)
  version  V1.0
  date  2021-01-14
  @get from https://www.dfrobot.com
  @url https://github.com/DFRobot/DFRobot_raspberrypi_upsSensor
"""
import serial
import time
import smbus

I2C_ADDRESS               = 0x58          # i2c slave Address


ERROR                     = -1.0

SET_TIME                  = 0x02

SET_ONE_STARTING_UP       = 0x03
SET_ONE_SHUTDOWN          = 0x04

SET_YEAR_STARTING_UP      = 0x05
SET_YEAR_SHUTDOWN         = 0x06

SET_MONTH_STARTING_UP     = 0x07
SET_MONTH_SHUTDOWN        = 0x08

SET_TWO_WEEK_STARTING_UP  = 0x09
SET_TWO_WEEK_SHUTDOWN     = 0x0a

SET_WEEK_STARTING_UP      = 0x0b
SET_WEEK_SHUTDOWN         = 0x0c

SET_DATE_STARTING_UP      = 0x0d
SET_DATE_SHUTDOWN         = 0x0e

SET_ONE_ALARM_STARTING_UP = 0x0f
SET_ONE_ALARM_SHUTDOWN    = 0x10

SET_ALARM_STARTING_UP     = 0x11
SET_ALARM_SHUTDOWN        = 0x12

CLEAR_LIST                = 0x13
CLEAR_LIST_ALL            = 0x14
GET_TIME                  = 0x15
GET_ELECTRIC              = 0x16
GET_PLAN_LEN              = 0x17

GET_PLAN_1                = 0x18
GET_PLAN_2                = 0x19
GET_PLAN_3                = 0x1a
GET_PLAN_4                = 0x1b
GET_PLAN_5                = 0x1c
GET_PLAN_6                = 0x1d
GET_PLAN_7                = 0x1e
GET_PLAN_8                = 0x1f
GET_PLAN_9                = 0x20
GET_PLAN_10               = 0x21
GET_PLAN_11               = 0x22
GET_PLAN_12               = 0x23
GET_PLAN_13               = 0x24
GET_PLAN_14               = 0x25
GET_PLAN_15               = 0x26
GET_PLAN_16               = 0x27
GET_PLAN_17               = 0x28
GET_PLAN_18               = 0x29
GET_PLAN_19               = 0x2a
GET_PLAN_20               = 0x2b
GET_PLAN_ALL              = 0xFF

AT_START_UP               = 1
AT_SHUTDOWN               = 2
AT_ALARM_START_UP         = 3
AT_ALARM_SHUTDOWN         = 4

PERIOD_ONCE               = 10
PERIOD_ONE_YEAR           = 1
PERIOD_ONE_MONTH          = 2
PERIOD_TWO_WEEK           = 3
PERIOD_ONE_WEEK           = 4
PERIOD_ONE_DATE           = 5
PERIOD_ALARM              = 6
PERIOD_ALARM_ONCE         = 7




class per_vol:
  def __init__(self):
    self.percentage = 0.0
    self.voltage    = 0.0     # ³ß´ç
temp_per = per_vol()

'''
   # time_struct 
   # year        range (2000 to 2100)
   # month       range (1    to 12)
   # date        range (1    to 31)  # There are 29 days in February in a leap year 
   # hour        range (0    to 23)
   # minute      range (0    to 59)
   # second      range (0    to 59)
'''
class time_struct:
  def __init__(self):
    self.year   = 0
    self.month  = 0
    self.date   = 0
    self.hour   = 0
    self.minute = 0
    self.second = 0
temp_time = time_struct()


class alarm_time_struct:
  def __init__(self):
    self.hour   = 0
    self.minute = 0
    self.second = 0
    self.types  = 0
    self.period = 0

class plan_struct:
  def __init__(self):
    self.year      = 0
    self.month     = 0
    self.date      = 0
    self.hour      = 0
    self.minute    = 0
    self.second    = 0
    self.types     = 0
    self.period    = 0
    self.n_year   = 0
    self.n_month  = 0
    self.n_date   = 0
    self.n_hour   = 0
    self.n_minute = 0
    self.n_second = 0
    self.period_string = ""
temp_plan = plan_struct()

class DFRobot_raspberrypi_ups(object): 
  __txbuf        = [0]          # i2c send buffer
  def __init__(self ,bus):
    self.i2cbus = smbus.SMBus(bus)

  '''
    @brief check date
    @param year
    @param month
    @param date
    @param hour
    @param minute
    @param second
    @return 0 or 1 (1 is date true , 0 is date false)
  '''
  def check_date(self ,year ,month ,date ,hour ,minute ,second):
    __month = [31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
    if year > 2100 or year < 2000:
      return 0
    if month == 2:
      if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
        __month[2] = 29;
    if month>12 or month<1 or date>__month[month-1] or date<1:
      return 0
    if hour   > 23 or hour   < 0:
      return 0
    if minute > 59 or minute < 0:
      return 0
    if second > 59 or second < 0:
      return 0
    return 1

  '''
    @brief analysis week 
    @param number is ananlysis data
  '''
  def analysis_week(self ,number):
    temp_string = ""
    for i in range(1,8):
      if number&0x01 == 1:
        temp_string = temp_string + str(i)
      number = number>>1
    if temp_string != "":
      temp_string = "/" + temp_string
    temp_plan.period_string = temp_string 
    
  '''
    @brief check hour 
    @param hour 
    @param minute
    @param second
    @return 0 or 1 (1 is hour true , 0 is hour false)
  '''
  def check_hour(self ,hour ,minute ,second):
    if hour   > 23 or hour   < 0:
      return 0
    if minute > 59 or minute < 0:
      return 0
    if second > 59 or second < 0:
      return 0
    return 1

  '''
    @brief set time
    @param s_time is time_struct
    @return 0 or 1 (1 is true , 0 is time error)
  '''
  def set_time(self ,s_time):
    if self.check_date(s_time.year,s_time.month,s_time.date,s_time.hour,s_time.minute,s_time.second) == 0:
      return 0
    txbuf     = [0]*8
    txbuf[0]  = SET_TIME
    txbuf[1]  = int(s_time.year) >> 8
    txbuf[2]  = s_time.year
    txbuf[3]  = s_time.month
    txbuf[4]  = s_time.date
    txbuf[5]  = s_time.hour
    txbuf[6]  = s_time.minute
    txbuf[7]  = s_time.second
    self.write_reg(SET_TIME ,txbuf)
    return 1

  '''
    @brief get the percentage and voltage value of the battery.
    @return percentage and voltage 
  '''
  def get_electric(self):
    self.__txbuf[0] = GET_ELECTRIC
    self.write_reg(GET_ELECTRIC ,self.__txbuf)
    rslt = self.read_reg(GET_ELECTRIC ,5)
    if rslt[0] == GET_ELECTRIC:
      percentage = float(rslt[1]) + float(rslt[2] / 100.0)
      voltage = rslt[3]*256 + rslt[4]
      temp_per.percentage = percentage
      temp_per.voltage    = voltage
      return temp_per
    else:
      temp_per.percentage = 0.0
      temp_per.voltage    = 0.0
      return temp_per

  '''
    @brief get plan len
    @return paln number or error
  '''
  def get_plan_len(self):
    self.__txbuf[0] = GET_PLAN_LEN
    self.write_reg(GET_PLAN_LEN ,self.__txbuf)
    rslt = self.read_reg(GET_PLAN_LEN ,2)
    if rslt[0] == GET_PLAN_LEN:
      return rslt[1]
    else:
      return -1

  '''
    @brief get plan list
    @param paln_number is plan number
    @return plan_struct
  '''
  def get_plan_list(self, plan_number):
    len = self.get_plan_len()
    if len == -1 or len == 0:
      temp_plan.year     = -1
      temp_plan.month    = -1
      temp_plan.date     = -1
      temp_plan.hour     = -1
      temp_plan.minute   = -1
      temp_plan.second   = -1
      temp_plan.types    = -1
      temp_plan.period   = -1
      temp_plan.n_year   = -1
      temp_plan.n_month  = -1
      temp_plan.n_date   = -1
      temp_plan.n_hour   = -1
      temp_plan.n_minute = -1
      temp_plan.n_second = -1
      temp_plan.period_string = ""
      return temp_plan
    else:
      self.__txbuf[0] = plan_number
      self.write_reg(plan_number ,self.__txbuf)  
      rslt = self.read_reg(plan_number ,20)
      if rslt[0] == plan_number:
        temp_plan.types   = rslt[1]
        temp_plan.period  = rslt[2]
        if rslt[2] == PERIOD_ALARM or rslt[2] == PERIOD_ALARM_ONCE:
          temp_plan.hour   = rslt[3]
          temp_plan.minute = rslt[4]
          temp_plan.second = rslt[5]
          self.analysis_week(rslt[6])
          temp_plan.n_year   = rslt[7]*256+rslt[8]  
          temp_plan.n_month  = rslt[9]
          temp_plan.n_date   = rslt[10]
          temp_plan.n_hour   = rslt[11]
          temp_plan.n_minute = rslt[12]
          temp_plan.n_second = rslt[13]
          return temp_plan
        else:
          temp_plan.year   = rslt[3]*256+rslt[4]
          temp_plan.month  = rslt[5]
          temp_plan.date   = rslt[6]
          temp_plan.hour   = rslt[7]
          temp_plan.minute = rslt[8]
          temp_plan.second = rslt[9]
          if rslt[2] == PERIOD_ONCE:
            temp_plan.period_string = ""
          elif rslt[2] == PERIOD_ONE_MONTH:
            temp_plan.period_string = "/M"
          elif rslt[2] == PERIOD_ONE_YEAR:
            temp_plan.period_string = "/Y"
          elif rslt[2] == PERIOD_TWO_WEEK:
            temp_plan.period_string = "/2W"
          elif rslt[2] == PERIOD_ONE_WEEK:
            temp_plan.period_string = "/W"
          elif rslt[2] == PERIOD_ONE_DATE:
            temp_plan.period_string = "/D"
          else:
            temp_plan.period_string = ""  
          temp_plan.n_year   = rslt[11]*256+rslt[12]  
          temp_plan.n_month  = rslt[13]
          temp_plan.n_date   = rslt[14]
          temp_plan.n_hour   = rslt[15]
          temp_plan.n_minute = rslt[16]
          temp_plan.n_second = rslt[17]
          return temp_plan
      else:
        temp_plan.year     = -1
        temp_plan.month    = -1
        temp_plan.date     = -1
        temp_plan.hour     = -1
        temp_plan.minute   = -1
        temp_plan.second   = -1
        temp_plan.types    = -1
        temp_plan.period   = -1
        temp_plan.n_year   = -1
        temp_plan.n_month  = -1
        temp_plan.n_date   = -1
        temp_plan.n_hour   = -1
        temp_plan.n_minute = -1
        temp_plan.n_second = -1
        temp_plan.period_string = ""
        return temp_plan

  '''
    @brief get time
    @return time struct
  '''
  def get_time(self):
    self.__txbuf[0] = GET_TIME
    self.write_reg(GET_TIME ,self.__txbuf)
    rslt = self.read_reg(GET_TIME ,8)
    if rslt[0] == GET_TIME:
      temp_time.year   = rslt[1]*256 + rslt[2]
      temp_time.month  = rslt[3]
      temp_time.date   = rslt[4]
      temp_time.hour   = rslt[5]
      temp_time.minute = rslt[6]
      temp_time.second = rslt[7]
      return temp_time
    else:
      temp_time.year   = 0
      temp_time.month  = 0
      temp_time.date   = 0
      temp_time.hour   = 0
      temp_time.minute = 0
      temp_time.second = 0
      return temp_time

  '''
    @brief set at time (You need to set the year, month, day, minute and second)
    @param time struct
    @return Is the time set correct
  '''
  def set_at_time(self ,s_time):
    if self.check_date(s_time.year,s_time.month,s_time.date,s_time.hour,s_time.minute,s_time.second) == 0:
      return 0
    txbuf     = [0]*8
    txbuf[0]  = s_time.types
    txbuf[1]  = int(s_time.year) >> 8
    txbuf[2]  = s_time.year
    txbuf[3]  = s_time.month
    txbuf[4]  = s_time.date
    txbuf[5]  = s_time.hour
    txbuf[6]  = s_time.minute
    txbuf[7]  = s_time.second
    self.write_reg(s_time.types ,txbuf)
    return 1

  '''
    @brief set alarm time (You need to set the hour, minute, second, don't need year and month and date)
    @param s_time is alarm_time_struct
    @return Is the time set correct
  '''
  def set_alarm_time(self ,s_time):
    if self.check_hour(s_time.hour,s_time.minute,s_time.second) == 0:
      return 0
    txbuf     = [0]*5
    txbuf[0]  = s_time.types
    txbuf[1]  = s_time.hour
    txbuf[2]  = s_time.minute
    txbuf[3]  = s_time.second
    txbuf[4]  = s_time.period
    self.write_reg(s_time.types ,txbuf)
    return 1

  '''
    @brief clean all plan
    @return (1 is clear success) ,(0 is clear error)
  '''
  def clear_plan_all(self):
    len = self.get_plan_len()
    if len == 0 or len == -1:
      return 0
    else:
      self.__txbuf[0] = CLEAR_LIST_ALL
      self.write_reg(CLEAR_LIST_ALL ,self.__txbuf)
      return 1

  '''
    @brief clean plan
    @param number is clear number
    @return (1 is clear success) ,(0 is clear error)
  '''
  def clear_plan(self ,number):
    len = self.get_plan_len()
    if len == 0 or len == -1:
      return 0
    elif number > len:
      return 0
    else:
      txbuf    = [0]*2
      txbuf[0] = CLEAR_LIST
      txbuf[1] = number
      self.write_reg(CLEAR_LIST ,txbuf)
      return 1

'''
  @brief An example of an i2c interface module
'''
class DFRobot_raspberrypi_ups_I2C(DFRobot_raspberrypi_ups): 
  def __init__(self ,bus ,addr):
    self.__addr = addr;
    super(DFRobot_raspberrypi_ups_I2C, self).__init__(bus)

  '''
    @brief writes data to a register
    @param reg register address
    @param value written data
  '''
  def write_reg(self, reg, data):
    while 1:
      try:
        self.i2cbus.write_i2c_block_data(self.__addr ,reg ,data)
        return
      except:
        print("please check connect!")
        time.sleep(1)
  '''
    @brief read the data from the register
    @param reg register address
    @param value read data
  '''
  def read_reg(self, reg ,len):
    while 1:
      try:
        rslt = self.i2cbus.read_i2c_block_data(self.__addr ,reg ,len)
        return rslt
      except:
        print("please check connect!")
        time.sleep(1)