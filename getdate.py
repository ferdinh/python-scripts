# get today's and utc's date and time
import datetime
from enum import Enum


class TimeCoordinate(Enum):
    """Represent date localization."""
    UTC = 1
    Local = 2


today = datetime.datetime.today()
utc = datetime.datetime.utcnow()

print("Current time: ", today)
print("UTC time: ", utc)

x = 0

while x == 0:
    z = input("View UTC or local? ")
    y = input("View hours, minutes, or seconds, or terminate? ")
    if z == "local" and y == "hours":
        print(today.hour)
    elif z == "local" and y == "minutes":
        print(today.minute)
    elif z == "local" and y == "seconds":
        print(today.second)
    elif z == "UTC" and y == "hours":
        print(utc.hour)
    elif z == "UTC" and y == "seconds":
        print(utc.second)
    elif z == "UTC" and y == "minutes":
        print(utc.minute)
    else:
        x = 1
def getTime(localization: TimeCoordinate = TimeCoordinate.Local) -> datetime:
    """Get current datetime based on specified localization"""
    currentTime: datetime

    if localization == TimeCoordinate.UTC:
        currentTime = datetime.datetime.utcnow()
    elif localization == TimeCoordinate.Local:
        currentTime = datetime.datetime.today()

    return currentTime
