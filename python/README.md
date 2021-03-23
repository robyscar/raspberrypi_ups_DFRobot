# DFRobot raspberrypi ups

This RaspberryPi ups can communicate with RaspberryPi via I2C.<br>


## DFRobot raspberrypi ups Library for RaspberryPi

Provide the Raspberry Pi library for the DFRobot_raspberrypi_ups module.

## Table of Contents

* [Summary](#summary)
* [Feature](#feature)
* [Installation](#installation)
* [Methods](#methods)
* [History](#history)
* [Credits](#credits)

## Summary

DFRobot_raspberrypi_ups module.

## Feature

1. With UPS you can control when the Raspberry Pi is on and off. <br>
2. You can get the battery power and the percentage. <br>

## Installation

This sensor should be connected to the I2C Raspberry Pi. <br>
Run the program:

```
$> python clear_plan.py
$> python get_electric.py
$> python get_plan_list.py
$> python set_alarm.py
$> python set_get_time.py
```

## Methods

```py


  class time_struct:
    '''
       # time_struct 
       # year        range (2000 to 2100)
       # month       range (1    to 12)
       # date        range (1    to 31)  # There are 29 days in February in a leap year 
       # hour        range (0    to 23)
       # minute      range (0    to 59)
       # second      range (0    to 59)
    '''

  class alarm_time_struct:
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

  class plan_struct:
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
  def check_date(self ,year ,month ,date ,hour ,minute ,second):
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

  def check_hour(self ,hour ,minute ,second):
    '''
      @brief check hour
      @param hour
      @param minute
      @param second
      @return 0 or 1 (1 is hour true , 0 is hour false)
    '''

  def analysis_week(self ,number):
    '''
      @brief analysis week 
      @param number is ananlysis data
    '''

  def set_time(self ,s_time):
    '''
      @brief set time
      @param s_time is time_struct
      @return 0 or 1 (1 is true , 0 is time error)
    '''

  def get_electric(self):
    '''
      @brief get the percentage and voltage value of the battery.
      @return percentage and voltage 
    '''

  def get_plan_len(self):
    '''
      @brief get plan len
      @return paln number or error
    '''

  def get_plan_list(self, plan_number):
    '''
      @brief get plan list
      @param paln_number is plan number
      @return plan_struct
    '''

  def get_time(self):
    '''
      @brief get time
      @return time struct
    '''

  def set_at_time(self ,s_time):
    '''
      @brief set at time (You need to set the year, month, day, minute and second)
      @param time struct
      @return Is the time set correct
    '''

  def set_alarm_time(self ,s_time):
    '''
      @brief set alarm time (You need to set the hour, minute, second, don't need year and month and date)
      @param s_time is alarm_time_struct
      @return Is the time set correct
    '''

  def clear_plan_all(self):
    '''
      @brief clean all plan
      @return (1 is clear success) ,(0 is clear error)
    '''

  def clear_plan(self ,number):
    '''
      @brief clean plan
      @param number is clear number
      @return (1 is clear success) ,(0 is clear error)
  '''
```
## History

January 29, 2021 - Version 1.0 released.

## Credits

Written by ZhixinLiu(zhixin.liu@dfrobot.com), 2021. (Welcome to our website)