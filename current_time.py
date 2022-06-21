# current_time.py
# - A script to display the current
#   time and date.

import datetime

def DateTimePretty():
    now = datetime.datetime.now()
    return now.strftime('%H:%M on %A, %B the %dth, %Y')
    # output: 12:30 on Friday, December the 29th, 2018

def TimeDate():
    now = now = datetime.datetime.now()
    return now.strftime("%m-%d-%Y_%H:%M")
    # output 12-29-2018_12:30
