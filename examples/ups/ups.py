# -*- coding:utf-8 -*-
""" 
  @file ups.py
  @brief ups function.
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @licence     The MIT License (MIT)
  @author      [ZhixinLiu](zhixin.liu@dfrobot.com)
  version  V1.0
  date  2021-01-27
  @get from https://www.dfrobot.com
  @url https://github.com/DFRobot/DFRobot_raspberrypi_ups
"""
import sys,os,argparse
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


def main():
  init_command()

def init_command():
  parser = argparse.ArgumentParser(description="For example, use the (python *.py -ups_example)")
  parser.add_argument("-year"           ,help="year   range   2000 to 2100" ,type=int   ,required=False)
  parser.add_argument("-month"          ,help="month  range      1 to 12  " ,type=int   ,required=False)
  parser.add_argument("-date"           ,help="date   range      1 to 31  " ,type=int   ,required=False)
  parser.add_argument("-hour"           ,help="hour   range      0 to 23  " ,type=int   ,required=False)
  parser.add_argument("-minute"         ,help="minute range      0 to 59  " ,type=int   ,required=False)
  parser.add_argument("-second"         ,help="second range      0 to 59  " ,type=int   ,required=False)
  parser.add_argument("-period"         ,help="period range      0 to 59  " ,type=bytes ,required=False)
  parser.add_argument("-get_plan"       ,help="get plan number   1 to 20  " ,type=int   ,required=False)
  parser.add_argument("-clear_plan"     ,help="clear plan number 1 to 20  " ,type=int   ,required=False)  
  parser.add_argument("-clear_plan_all" ,help="Clear all plans"                    ,action='store_true')
  parser.add_argument("-ups_example"    ,help="ups all example"                    ,action='store_true')
  parser.add_argument("-get_electric"   ,help="get electric"                       ,action='store_true')
  parser.add_argument("-get_time"       ,help="get ups time"                       ,action='store_true')
  parser.add_argument("-get_plan_len"   ,help="get plan number"                    ,action='store_true')
  parser.add_argument("-get_plan_all"   ,help="get plan list all"                  ,action='store_true')
  parser.add_argument("-set_time"       ,help="Set ups time."                      ,action='store_true')
  parser.add_argument("-set_one_up"     ,help="Set a boot time."                   ,action='store_true')
  parser.add_argument("-set_one_down"   ,help="Set a shutdown time."               ,action='store_true')
  parser.add_argument("-set_year_up"    ,help="Set up an annual cycle start."      ,action='store_true')
  parser.add_argument("-set_year_down"  ,help="Set the shutdown cycle in years."   ,action='store_true')
  parser.add_argument("-set_month_up"   ,help="Set a monthly cycle."               ,action='store_true')
  parser.add_argument("-set_month_down" ,help="Set a monthly shutdown."            ,action='store_true')
  parser.add_argument("-set_tweek_up"   ,help="Set a two-week cycle boot."         ,action='store_true')
  parser.add_argument("-set_tweek_down" ,help="Set a two-week cycle shutdown."     ,action='store_true')
  parser.add_argument("-set_week_up"    ,help="Set a weekly boot."                 ,action='store_true')
  parser.add_argument("-set_week_down"  ,help="Set a weekly shutdown."             ,action='store_true')
  parser.add_argument("-set_date_up"    ,help="Set a day-cycle boot."              ,action='store_true')
  parser.add_argument("-set_date_down"  ,help="Set a day-cycle shutdown."          ,action='store_true')
  parser.add_argument("-set_one_alarm_up"    ,help="Set a boot Alarm ,Don't need a period."       ,action='store_true')
  parser.add_argument("-set_one_alarm_down"  ,help="Set a shutdown Alarm ,Don't need a period."   ,action='store_true')
  parser.add_argument("-set_loop_alarm_up"   ,help="set the loop boot alarm, need a period."      ,action='store_true')
  parser.add_argument("-set_loop_alarm_down" ,help="set the loop shutdown alarm, need a period."  ,action='store_true')
  args = parser.parse_args()
  if args.ups_example:
    ups_example()
  elif args.get_electric:
    read_electric()
  elif args.get_time:
    read_time()
  elif args.get_plan_len:
    read_plan_len()
  elif args.get_plan_all:
    read_plan_all()
  elif args.get_plan:
    read_plan(args.get_plan)
  elif args.clear_plan_all:
    set_clear_all()
  elif args.clear_plan:
    set_clear_plan(args.clear_plan)
  elif args.set_time and args.year and args.month and args.date and args.hour and args.minute and args.second:
    write_time(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second)
  elif args.set_one_up and args.year and args.month and args.date and args.hour and args.minute and args.second:
    set_at(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second,SET_ONE_STARTING_UP)
  elif args.set_one_down and args.year and args.month and args.date and args.hour and args.minute and args.second:
    set_at(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second,SET_ONE_SHUTDOWN)
  elif args.set_year_up and args.year and args.month and args.date and args.hour and args.minute and args.second:
    set_at(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second,SET_YEAR_STARTING_UP)
  elif args.set_year_up and args.year and args.month and args.date and args.hour and args.minute and args.second:
    set_at(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second,SET_YEAR_SHUTDOWN)
  elif args.set_month_up and args.year and args.month and args.date and args.hour and args.minute and args.second:
    set_at(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second,SET_MONTH_STARTING_UP)
  elif args.set_month_down and args.year and args.month and args.date and args.hour and args.minute and args.second:
    set_at(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second,SET_MONTH_SHUTDOWN)
  elif args.set_tweek_up and args.year and args.month and args.date and args.hour and args.minute and args.second:
    set_at(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second,SET_TWO_WEEK_STARTING_UP)
  elif args.set_tweek_down and args.year and args.month and args.date and args.hour and args.minute and args.second:
    set_at(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second,SET_TWO_WEEK_SHUTDOWN)
  elif args.set_week_up and args.year and args.month and args.date and args.hour and args.minute and args.second:
    set_at(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second,SET_WEEK_STARTING_UP)
  elif args.set_week_down and args.year and args.month and args.date and args.hour and args.minute and args.second:
    set_at(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second,SET_WEEK_SHUTDOWN)
  elif args.set_date_up and args.year and args.month and args.date and args.hour and args.minute and args.second:
    set_at(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second,SET_DATE_STARTING_UP)
  elif args.set_date_down and args.year and args.month and args.date and args.hour and args.minute and args.second:
    set_at(args.year ,args.month ,args.date ,args.hour ,args.minute ,args.second,SET_ALARM_SHUTDOWN)
  elif args.set_one_alarm_up and args.hour and args.minute and args.second:
    set_alarm(args.hour ,args.minute ,args.second,SET_ONE_ALARM_STARTING_UP)
  elif args.set_one_alarm_down and args.hour and args.minute and args.second:
    set_alarm(args.hour ,args.minute ,args.second,SET_ONE_ALARM_SHUTDOWN)
  elif args.set_loop_alarm_up and args.hour and args.minute and args.second and args.period:
    set_alarm(args.hour ,args.minute ,args.second,SET_ALARM_STARTING_UP ,int(args.period ,2))
  elif args.set_loop_alarm_down and args.hour and args.minute and args.second and args.period:
    set_alarm(args.hour ,args.minute ,args.second,SET_ALARM_SHUTDOWN ,int(args.period ,2))
  else:
    print "Parameter does not match, please get prompt eg: python ups.py -ups_example"

def ups_example():
  print "(2000 < year < 2100) (1 < month  < 12) (1 < date   < 31)  |Year, month and day range"
  print "(0 < hour < 23)      (0 < minute < 59) (0 < second < 59)  |Hour, minute, second range"
  print "period is cycle week"
  print " ________________________________________________________________________"
  print "|reserve |sunday |saturday |Friday |Thursday |Wednesday |Tuesday |Monday |"
  print "|0       |0      |0        |0      |0        |0         |0       |0      |"
  print "|________|_______|_________|_______|_________|__________|________|_______|"
  print "eg: 0b00000001 is monday"
  print "    0b00100001 is saturday ,monday"
  print "    0b01111111 is sunday ,saturday ,Friday ,Thursday ,Wednesday ,Tuesday ,Monday"
  print ""
  print "1.  get_time         eg:   python *.py -get_time"
  print "2.  get_electric     eg:   python *.py -get_electric"
  print "3.  ups_example      eg:   python *.py -ups_example"
  print "4.  get_plan         eg    python *.py -get_plan (1-20)"
  print "5.  get_plan_all     eg:   python *.py -get_plan_all"
  print "6.  get_plan_len     eg:   python *.py -get_plan_len"
  print "7.  clear_plan       eg    python *.py -clear_plan (1-20)"
  print "8.  clear_plan_all   eg:   python *.py -clear_plan_all"
  print "9.  set time         eg:   python *.py -set_time -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"
  print "10. set_one_up       eg:   python *.py -set_one_up -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"
  print "11. set_one_down     eg:   python *.py -set_one_down -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"
  print "12. set_year_up      eg:   python *.py -set_year_up -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"
  print "13. set_year_down    eg:   python *.py -set_year_down -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"
  print "14. set_month_up     eg:   python *.py -set_month_up -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"
  print "15. set_month_down   eg:   python *.py -set_month_down -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"
  print "16. set_tweek_up     eg:   python *.py -set_tweek_up -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"
  print "17. set_tweek_down   eg:   python *.py -set_tweek_down -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"
  print "18. set_week_up      eg:   python *.py -set_week_up -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"
  print "19. set_week_down    eg:   python *.py -set_week_down -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"
  print "20. set_date_up      eg:   python *.py -set_date_up -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"
  print "21. set_date_down    eg:   python *.py -set_date_down -year 2020 -month 2 -date 3 -hour 10 -minute 10 -second 10"  
  print "22. set_one_alarm_up      eg:   python *.py -set_one_alarm_up -hour 10 -minute 10 -second 10"
  print "23. set_one_alarm_down    eg:   python *.py -set_one_alarm_down -hour 10 -minute 10 -second 10"
  print "24. set_loop_alarm_up     eg:   python *.py -set_loop_alarm_up -hour 10 -minute 10 -second 10 -period 0b01111111"
  print "25. set_loop_alarm_down   eg:   python *.py -set_loop_alarm_down -hour 10 -minute 10 -second 10 -period 0b01111111"

def set_at(year ,month ,date ,hour ,minute ,second ,types):
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
  oldnum = ups.get_plan_len()
  timedata = time_struct()
  timedata.year   = year
  timedata.month  = month
  timedata.date   = date
  timedata.hour   = hour
  timedata.minute = minute
  timedata.second = second
  timedata.types  = types
  if ups.set_at_time(timedata) != 1:
    print "Please check whether the time is correct!"
  else:
    newnum = ups.get_plan_len()
    if oldnum == newnum:
      print "Set the alarm to last longer than the current time!"
    else:
      print "set success!"

def set_alarm(hour ,minute ,second ,types ,period=0):
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
  alarmdata.hour   = hour
  alarmdata.minute = minute
  alarmdata.second = second
  alarmdata.types  = types
  alarmdata.period = period
  if ups.set_alarm_time(alarmdata) != 1:
    print "Please check whether the time is correct!"
  else:
    print "set alarm success!"

def set_clear_all():
  if ups.clear_plan_all() == 1:
    print "clear success!"
  else:
    print "The list is empty! clear false!"

def set_clear_plan(number):
  num = ups.get_plan_len()
  if num == -1:
    print "clear plan error"
    return
  elif num == 0:
    print "plan list is empty"
    return
  elif num < number:
    print "plan is no exist"
    return
  else:
    if ups.clear_plan(number) == 1:
      print "clear success!"
    else:
      print "clear false! please check plan list"

def write_time(year ,month ,date ,hour ,minute ,second):
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
  timedata.year   = year
  timedata.month  = month
  timedata.date   = date
  timedata.hour   = hour
  timedata.minute = minute
  timedata.second = second
  if ups.set_time(timedata) == 1:
    print "set time success!"
  else:
    print "set time false! please check whether the time is correct!"

def read_electric():
  data = ups.get_electric()
  print("voltage    = %d  mv"%data.voltage)
  print("percentage = %.2f %%"%data.percentage)

def read_time():
  data = ups.get_time()              # Data contains (year ,month ,date ,hour ,minute ,second)
  print("%d/%d/%d/%d:%d:%d"%(data.year,data.month,data.date,data.hour,data.minute,data.second))

def read_plan_len():
  number = ups.get_plan_len()
  if number != -1:
    print("There are %d plans"%number)
  else:
    print "get plan error"

def read_plan_all():
  number = ups.get_plan_len()
  if number == -1:
    print "get plan error"
    return
  elif number == 0:
    print "plan list is empty"
    return
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

def read_plan(number):
  num = ups.get_plan_len()
  if num == -1:
    print "get plan error"
    return
  elif num == 0:
    print "plan list is empty"
    return
  elif num < number:
    print "plan is no exist"
    return
  plan_list = ups.get_plan_list(GET_PLAN_1+number-1)
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

if __name__ == "__main__":
  main()