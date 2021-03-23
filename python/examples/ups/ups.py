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
  parser = argparse.ArgumentParser(description="For example, use the (python ups.py -p help)")
  parser.add_argument("-p" ,help="Please enter the correct instructions." ,type=str)
  args = parser.parse_args()
  if args.p:
    parse_string(args.p)
  else:
    print "Parameter does not match, please get prompt eg: python ups.py -p help"

'''
  @brief parsed string
'''
def parse_string(string):
  if string == "get_time":
    read_time()
  elif string == "read_time":
    read_time_test()
  elif string == "get_electric":
    read_electric()
  elif string == "help":
    ups_example()
  elif string == "get_plan_len":
    read_plan_len()
  elif string == "get_plan_all":
    read_plan_all()
  elif string == "clear_plan_all":
    set_clear_all()
  elif string[0:11] == "clear_plan=":
    string_len = len(string)
    if string_len == 12:
      if string[11] >= '0' and string[11] <= '9':
        set_clear_plan(int(string[11]))
    elif string_len == 13:
      if string[11] >= '0' and string[11] <= '9' and string[12] >= '0' and string[12] <= '9':
        if int(string[11:13]) > 20 or int(string[11:13]) < 1:
          print "number error!"
        else:
          set_clear_plan(int(string[11:13]))
      else:
        print "string error!"
    else:
      print "command error!"
  elif string[0:9] == "get_plan=":
    string_len = len(string)
    if string_len == 10:
      if string[9] >= '0' and string[9] <= '9':
        read_plan(int(string[9]))
    elif string_len == 11:
      if string[9] >= '0' and string[9] <= '9' and string[10] >= '0' and string[10] <= '9':
        if int(string[9:11]) > 20 or int(string[9:11]) < 1:
          print "number error!"
        else:
          read_plan(int(string[9:11]))
      else:
        print "string error!"
    else:
      print "command error!"
  elif string[0:9] == "shutdown=":
    string_len  = len(string)
    backslash   = string.count('/' ,9)
    colon       = string.count(':' ,9)
    if backslash == 3 and colon == 2:
      backslash_1 = string.index('/' ,9)
      backslash_2 = string.index('/' ,backslash_1+1)
      backslash_3 = string.index('/' ,backslash_2+1)
      colon_1 = string.index(':' ,backslash_3)
      colon_2 = string.index(':' ,colon_1+1)
      year   = analysis_year(string ,9 ,backslash_1)
      month  = analysis_month(string ,backslash_1+1 ,backslash_2)
      date   = analysis_date(string ,backslash_2+1 ,backslash_3)
      hour   = analysis_hour(string ,backslash_3+1 ,colon_1)
      minute = analysis_minute(string ,colon_1+1 ,colon_2)
      second = analysis_second(string ,colon_2+1 ,string_len)
      if year == -1 or month == -1 or date == -1 or hour == -1 or minute == -1 or second == -1:
        print "date error!"
      else:
        set_at(year ,month ,date ,hour ,minute ,second,SET_ONE_SHUTDOWN)
    elif backslash == 4 and colon == 2:
      backslash_1 = string.index('/' ,9)
      backslash_2 = string.index('/' ,backslash_1+1)
      backslash_3 = string.index('/' ,backslash_2+1)
      colon_1 = string.index(':' ,backslash_3)
      colon_2 = string.index(':' ,colon_1+1)
      backslash_4 = string.index('/' ,colon_2+1)
      year   = analysis_year(string ,9 ,backslash_1)
      month  = analysis_month(string ,backslash_1+1 ,backslash_2)
      date   = analysis_date(string ,backslash_2+1 ,backslash_3)
      hour   = analysis_hour(string ,backslash_3+1 ,colon_1)
      minute = analysis_minute(string ,colon_1+1 ,colon_2)
      second = analysis_second(string ,colon_2+1 ,backslash_4)
      period = analysis_period(string ,backslash_4+1 ,string_len ,SHUTDOWN)
      if year == -1 or month == -1 or date == -1 or hour == -1 or minute == -1 or second == -1 or period == -1:
        print "date error!"
      else:
        set_at(year ,month ,date ,hour ,minute ,second ,period)
    else:
      print "command error!"
  elif string[0:12] == "starting_up=":
    string_len  = len(string)
    backslash   = string.count('/' ,12)
    colon       = string.count(':' ,12)
    if backslash == 3 and colon == 2:
      backslash_1 = string.index('/' ,12)
      backslash_2 = string.index('/' ,backslash_1+1)
      backslash_3 = string.index('/' ,backslash_2+1)
      colon_1 = string.index(':' ,backslash_3)
      colon_2 = string.index(':' ,colon_1+1)
      year   = analysis_year(string ,12 ,backslash_1)
      month  = analysis_month(string ,backslash_1+1 ,backslash_2)
      date   = analysis_date(string ,backslash_2+1 ,backslash_3)
      hour   = analysis_hour(string ,backslash_3+1 ,colon_1)
      minute = analysis_minute(string ,colon_1+1 ,colon_2)
      second = analysis_second(string ,colon_2+1 ,string_len)
      if year == -1 or month == -1 or date == -1 or hour == -1 or minute == -1 or second == -1:
        print "date error!"
      else:
        set_at(year ,month ,date ,hour ,minute ,second,SET_ONE_STARTING_UP)
    elif backslash == 4 and colon == 2:
      backslash_1 = string.index('/' ,12)
      backslash_2 = string.index('/' ,backslash_1+1)
      backslash_3 = string.index('/' ,backslash_2+1)
      colon_1 = string.index(':' ,backslash_3)
      colon_2 = string.index(':' ,colon_1+1)
      backslash_4 = string.index('/' ,colon_2+1)
      year   = analysis_year(string ,9 ,backslash_1)
      month  = analysis_month(string ,backslash_1+1 ,backslash_2)
      date   = analysis_date(string ,backslash_2+1 ,backslash_3)
      hour   = analysis_hour(string ,backslash_3+1 ,colon_1)
      minute = analysis_minute(string ,colon_1+1 ,colon_2)
      second = analysis_second(string ,colon_2+1 ,backslash_4)
      period = analysis_period(string ,backslash_4+1 ,string_len ,SHUTDOWN)
      if year == -1 or month == -1 or date == -1 or hour == -1 or minute == -1 or second == -1 or period == -1:
        print "date error!"
      else:
        set_at(year ,month ,date ,hour ,minute ,second ,period)
    else:
      print "command error!"
    print string
  elif string[0:15] == "alarm_shutdown=":
    string_len  = len(string)
    backslash   = string.count('/' ,15)
    colon       = string.count(':' ,15)
    if backslash == 1 and colon == 2:
      colon_1     = string.index(':' ,15)
      colon_2     = string.index(':' ,colon_1+1)
      backslash_1 = string.index('/' ,colon_2+1)
      hour   = analysis_hour(string ,15 ,colon_1)
      minute = analysis_minute(string ,colon_1+1 ,colon_2)
      second = analysis_second(string ,colon_2+1 ,backslash_1)
      period = analysis_period(string ,backslash_1+1 ,string_len ,ALARM_SHUTDOWN)
      if hour == -1 or minute == -1 or second == -1 or period == -1:
        print "alarm data error!"
      else:
        set_alarm(hour ,minute ,second ,SET_ONE_ALARM_SHUTDOWN ,period)
    elif backslash == 0 and colon == 2:
      colon_1     = string.index(':' ,15)
      colon_2     = string.index(':' ,colon_1+1)
      hour   = analysis_hour(string ,15 ,colon_1)
      minute = analysis_minute(string ,colon_1+1 ,colon_2)
      second = analysis_second(string ,colon_2+1 ,string_len)
      if hour == -1 or minute == -1 or second == -1:
        print "alarm data error!"
      else:
        set_alarm(hour ,minute ,second ,SET_ONE_ALARM_SHUTDOWN)
    else:
      print "command error!"
  elif string[0:18] == "alarm_starting_up=":
    string_len  = len(string)
    backslash   = string.count('/' ,18)
    colon       = string.count(':' ,18)
    if backslash == 1 and colon == 2:
      colon_1     = string.index(':' ,18)
      colon_2     = string.index(':' ,colon_1+1)
      backslash_1 = string.index('/' ,colon_2+1)
      hour   = analysis_hour(string ,15 ,colon_1)
      minute = analysis_minute(string ,colon_1+1 ,colon_2)
      second = analysis_second(string ,colon_2+1 ,backslash_1)
      period = analysis_period(string ,backslash_1+1 ,string_len ,ALARM_START_UP)
      if hour == -1 or minute == -1 or second == -1 or period == -1:
        print "alarm data error!"
      else:
        set_alarm(hour ,minute ,second ,SET_ALARM_STARTING_UP ,period)
    elif backslash == 0 and colon == 2:
      colon_1     = string.index(':' ,18)
      colon_2     = string.index(':' ,colon_1+1)
      hour   = analysis_hour(string ,18 ,colon_1)
      minute = analysis_minute(string ,colon_1+1 ,colon_2)
      second = analysis_second(string ,colon_2+1 ,string_len)
      if hour == -1 or minute == -1 or second == -1:
        print "alarm data error!"
      else:
        set_alarm(hour ,minute ,second ,SET_ONE_ALARM_STARTING_UP)
    else:
      print "command error!"
  else:
    print "Please check the commands you entered!"
    print "Enter the command as prompted python!"
    print "eg:  python ups.py -p help"

'''
  @brief analysis year
  @return year
'''
def analysis_year(string ,begin ,end):
  if begin >= end:
    return -1;
  else:
    for i in range(begin ,end):
      if string[i] > '9' or string[i] < '0':
        return -1
    year = int(string[begin:end])
    if year > 2100 or year < 2000:
      return -1;
    else:
      return year
      
'''
  @brief analysis month
  @return month
'''
def analysis_month(string ,begin ,end):
  if begin >= end:
    return -1;
  else:
    for i in range(begin ,end):
      if string[i] > '9' or string[i] < '0':
        return -1
    month = int(string[begin:end])
    if month > 12 or month < 1:
      return -1;
    else:
      return month

'''
  @brief analysis date
  @return date
'''
def analysis_date(string ,begin ,end):
  if begin >= end:
    return -1;
  else:
    for i in range(begin ,end):
      if string[i] > '9' or string[i] < '0':
        return -1
    date = int(string[begin:end])
    if date > 31 or date < 1:
      return -1;
    else:
      return date

'''
  @brief analysis hour
  @return hour
'''
def analysis_hour(string ,begin ,end):
  if begin >= end:
    return -1;
  else:
    for i in range(begin ,end):
      if string[i] > '9' or string[i] < '0':
        return -1
    hour = int(string[begin:end])
    if hour > 31 or hour < 1:
      return -1;
    else:
      return hour

'''
  @brief analysis minute
  @return minute
'''
def analysis_minute(string ,begin ,end):
  if begin >= end:
    return -1;
  else:
    for i in range(begin ,end):
      if string[i] > '9' or string[i] < '0':
        return -1
    minute = int(string[begin:end])
    if minute > 59 or minute < 0:
      return -1;
    else:
      return minute

'''
  @brief analysis second
  @return second
'''
def analysis_second(string ,begin ,end):
  if begin >= end:
    return -1;
  else:
    for i in range(begin ,end):
      if string[i] > '9' or string[i] < '0':
        return -1
    second = int(string[begin:end])
    if second > 59 or second < 0:
      return -1;
    else:
      return second

'''
  @brief analysis second
  @return second
'''
def analysis_period(string ,begin ,end ,mode):
  period = 0
  if begin >= end:
    return -1;
  else:
    if mode == START_UP:
      if string[begin:end] == "Y":
        return SET_YEAR_STARTING_UP
      elif string[begin:end] == "M":
        return SET_MONTH_STARTING_UP
      elif string[begin:end] == "2W":
        return SET_TWO_WEEK_STARTING_UP
      elif string[begin:end] == "W":
        return SET_WEEK_STARTING_UP
      elif string[begin:end] == "D":
        return SET_DATE_STARTING_UP
      else:
        return -1
    elif mode == SHUTDOWN:
      if string[begin:end] == "Y":
        return SET_YEAR_SHUTDOWN
      elif string[begin:end] == "M":
        return SET_MONTH_SHUTDOWN
      elif string[begin:end] == "2W":
        return SET_TWO_WEEK_SHUTDOWN
      elif string[begin:end] == "W":
        return SET_WEEK_SHUTDOWN
      elif string[begin:end] == "D":
        return SET_DATE_SHUTDOWN
      else:
        return -1
    elif mode == ALARM_START_UP or mode == ALARM_SHUTDOWN:
      for i in range(begin ,end):
        if string[i] > '7' or string[i] < '1':
          return -1
        else:
          period = period | (1 << (int(string[i])-1))
      return period
    else:
      return -1

'''
    @brief get systm time
    @return time
'''
def get_sys_time():
  localtime = time.localtime(time.time())
  return localtime 

def ups_example():
  print "--------------------------------------------------------------------|"
  print "python ups.py -p help                                               |Get help information"
  print "python ups.py -p get_time                                           |synchronization time"
  print "python ups.py -p get_electric                                       |Get battery power (Percentage and voltage and state)"
  print "python ups.py -p get_plan_len                                       |Get plan list number"
  print "python ups.py -p get_plan_all                                       |Get all plan list"
  print "python ups.py -p get_plan=number                                    |Get time plan list (number is 1-20)"
  print "--------------------------------------------------------------------|"
  print "python ups.py -p clear_plan_all                                     |Clear all plan lists"
  print "python ups.py -p clear_plan=number                                  |Clear the list of which plan range:(1-20)"
  print "python ups.py -p clear_plan=1                                       |Clear the first plan"
  print "python ups.py -p clear_plan=20                                      |Clear the 20th plan"
  print "--------------------------------------------------------------------|"
  print "(2000 < year < 2100) (1 < month  < 12) (1 < date   < 31)            |Year, month and day range"
  print "(0 < hour < 23)      (0 < minute < 59) (0 < second < 59)            |Hour, minute, second range"
  print "--------------------------------------------------------------------|"
  print "python ups.py -p alarm_shutdown=hour:minute:second                  |Single alarm shutdown time"
  print "python ups.py -p alarm_starting_up=hour:minute:second               |Single alarm start time"
  print "python ups.py -p shutdown=year/month/date/hour:minute:second        |Set the time for a single shutdown"
  print "python ups.py -p starting_up=year/month/date/hour:minute:second     |Set the time for a single boot"
  print "--------------------------------------------------------------------|"
  print "python ups.py -p alarm_shutdown=hour:minute:second/?                |Alarm clock for days of the week"
  print "python ups.py -p alarm_shutdown=hour:minute:second/1357             |Closed every Monday, Wednesday, Friday, Sunday"
  print "--------------------------------------------------------------------|"
  print "python ups.py -p alarm_starting_up=hour:minute:second/?             |Alarm clock for days of the week"
  print "python ups.py -p alarm_starting_up==hour:minute:second/246          |Boot every Tuesday, Thursday, Saturday"
  print "--------------------------------------------------------------------|"
  print "python ups.py -p shutdown=year/month/date/hour:minute:second/?      |Set cycle shutdown"
  print "python ups.py -p shutdown=year/month/date/hour:minute:second/Y      |Cycle year"
  print "python ups.py -p shutdown=year/month/date/hour:minute:second/M      |Cycle month"
  print "python ups.py -p shutdown=year/month/date/hour:minute:second/2W     |Cycle two week"
  print "python ups.py -p shutdown=year/month/date/hour:minute:second/W      |Cycle week"
  print "python ups.py -p shutdown=year/month/date/hour:minute:second/D      |Cycle date"
  print "--------------------------------------------------------------------|"
  print "python ups.py -p starting_up=year/month/date/hour:minute:second/?   |Set cycle Boot up"
  print "python ups.py -p starting_up=year/month/date/hour:minute:second/Y   |Cycle year"
  print "python ups.py -p starting_up=year/month/date/hour:minute:second/M   |Cycle month"
  print "python ups.py -p starting_up=year/month/date/hour:minute:second/2W  |Cycle two week"
  print "python ups.py -p starting_up=year/month/date/hour:minute:second/W   |Cycle week"
  print "python ups.py -p starting_up=year/month/date/hour:minute:second/D   |Cycle date"
  print "--------------------------------------------------------------------|"	
'''
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
'''

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

def read_electric():
  data = ups.get_electric()
  print("voltage    = %d  mv"%data.voltage)
  print("percentage = %.2f %%"%data.percentage)
  if data.power_state == 1:
    print("Charging ")
  else:
    print("No charging")
  data = ups.get_time()              # Data contains (year ,month ,date ,hour ,minute ,second)
  #print("%d/%d/%d/%d:%d:%d"%(data.year,data.month,data.date,data.hour,data.minute,data.second))

def read_time_test():
  data = ups.get_time()
  print("%d/%d/%d/%d:%d:%d"%(data.year,data.month,data.date,data.hour,data.minute,data.second))

def read_time():
  nowtime = get_sys_time()
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
  timedata.year   = nowtime.tm_year
  timedata.month  = nowtime.tm_mon
  timedata.date   = nowtime.tm_mday
  timedata.hour   = nowtime.tm_hour
  timedata.minute = nowtime.tm_min
  timedata.second = nowtime.tm_sec
  print "current time is ",timedata.year,"/",timedata.month,"/",timedata.date,"/",timedata.hour,":",timedata.minute,":",timedata.second
  if ups.set_time(timedata) == 1:
    print "synchronization time success!"
  else:
    print "synchronization time false!"

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
    if plan_list.types == START_UP:
      print("%d - START_UP=%d/%d/%d/%d:%d:%d%s\t-next alarm- %d/%d/%d/%d:%d:%d"%(i+1,plan_list.year,plan_list.month,plan_list.date,\
      plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
      plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
    elif plan_list.types == SHUTDOWN:
      print("%d - SHUTDOWN=%d/%d/%d/%d:%d:%d%s\t-next alarm- %d/%d/%d/%d:%d:%d"%(i+1,plan_list.year,plan_list.month,plan_list.date,\
      plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
      plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
    elif plan_list.types == ALARM_START_UP:
      print("%d - ALARM_START_UP=%d:%d:%d%s\t-next alarm- %d/%d/%d/%d:%d:%d"%(i+1,plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
      plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
    elif plan_list.types == ALARM_SHUTDOWN:
      print("%d - ALARM_SHUTDOWN=%d:%d:%d%s\t-next alarm- %d/%d/%d/%d:%d:%d"%(i+1,plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
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
  if plan_list.types == START_UP:
    print("START_UP=%d/%d/%d/%d:%d:%d%s -next alarm- %d/%d/%d/%d:%d:%d"%(plan_list.year,plan_list.month,plan_list.date,\
    plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
    plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
  elif plan_list.types == SHUTDOWN:
    print("SHUTDOWN=%d/%d/%d/%d:%d:%d%s -next alarm- %d/%d/%d/%d:%d:%d"%(plan_list.year,plan_list.month,plan_list.date,\
    plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
    plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
  elif plan_list.types == ALARM_START_UP:
    print("ALARM_START_UP=%d:%d:%d%s -next alarm- %d/%d/%d/%d:%d:%d"%(plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
    plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
  elif plan_list.types == ALARM_SHUTDOWN:
    print("ALARM_SHUTDOWN=%d:%d:%d%s -next alarm- %d/%d/%d/%d:%d:%d"%(plan_list.hour,plan_list.minute,plan_list.second,plan_list.period_string,\
    plan_list.n_year,plan_list.n_month,plan_list.n_date,plan_list.n_hour,plan_list.n_minute,plan_list.n_second))
  else:
    print "get plan empty or error"

if __name__ == "__main__":
  main()