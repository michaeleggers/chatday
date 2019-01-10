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

utctime = datetime.datetime.utcnow()
munichUTC = datetime.timedelta(hours=1)
minnesotaUTC = datetime.timedelta(hours=-6)
londonUTC = datetime.timedelta(hours=0)
hongkongUTC = datetime.timedelta(hours=8)

localTargetTime = datetime.datetime(2019, month, day, hour, minutes)


targetUTC = munichUTC
if location == 'munich':
    targetUTC = localTargetTime + munichUTC
elif location == 'minnesota':
    targetUTC = localTargetTime + minnesotaUTC
elif location == 'london':
    targetUTC = localTargetTime + londonUTC
else: targetUTC = localTargetTime + hongkongUTC


print ("\nUTC times")

munichTargetUTC = localTargetTime + munichUTC
minnesotaTargetUTC = localTargetTime + minnesotaUTC
londonTargetUTC = localTargetTime + londonUTC
hongkongTargetUTC = localTargetTime + hongkongUTC

print ("Munich: \t" + str(munichTargetUTC))
print ("Minnesota: \t" + str(minnesotaTargetUTC))
print ("London: \t" + str(londonTargetUTC))
print ("Hong Kong: \t" + str(hongkongTargetUTC))

print ("\nlocalized times")
print ("Munich: \t" + str(localTargetTime + (munichTargetUTC - targetUTC)))
print ("Minnesota: \t" + str(localTargetTime + (minnesotaTargetUTC - targetUTC)))
print ("London: \t" + str(localTargetTime + (londonTargetUTC - targetUTC)))
print ("Hong Kong: \t" + str(localTargetTime + (hongkongTargetUTC - targetUTC)))
