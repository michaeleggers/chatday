# 
# Michael Eggers, eggers@hm.edu 1/10/2019
# Tool that converts local time to a different timezone (no daylight saving support, yet!)
# and only works for 2019, because why not. (I simply could add it as an argument but it is early in the year...)
# 
# Usage:
# python chatday.py <month> <day> <hours> <minutes> <location>
# where:
#   month = [1-12]
#   day = [1-31]
#   hours = [0-23] (military format)
#   minutes = [0-59]
#   location = munich | minnesota | london | hongkong
#

import datetime
import os
import argparse

parser = argparse.ArgumentParser(description="convert timezones")
parser.add_argument("month", metavar="month", type=int, help="month")
parser.add_argument("day", metavar="day", type=int, help="day")
parser.add_argument("hour", metavar="hour", type=int, help="hour")
parser.add_argument("minutes", metavar="minutes", type=int, help="minutes")
parser.add_argument("location", metavar="location", type=str, help="hometime")
args = parser.parse_args()

day = args.day
month = args.month
hour = args.hour
minutes = args.minutes
location = args.location

# for a new location, add location string and UTC offset to this dict.
location2UTC = {
    "munich" : 1,
    "minnesota" : -6,
    "london" : 0,
    "hongkong" : 8,
    "istanbul" : 3
}


localTargetTime = datetime.datetime(2019, month, day, hour, minutes)
targetUTC = localTargetTime + datetime.timedelta(hours=location2UTC.get(location))

location2targetUTC = {}
for location in location2UTC:
    location2targetUTC[location] = localTargetTime + datetime.timedelta(hours=location2UTC.get(location))

print ("\nUTC times")
for location in location2targetUTC:
    print(location + ": \t" + str(location2targetUTC.get(location)))

print ("\nlocalized times")
for location in location2targetUTC:
    print(location + ": \t" + str(localTargetTime + (location2targetUTC.get(location) - targetUTC)))
    
