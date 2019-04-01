# get today's and utc's date and time
import datetime
from enum import Enum


class TimeCoordinate(Enum):
    """Represent date localization."""
    UTC = 1
    Local = 2


def getTime(localization: TimeCoordinate = TimeCoordinate.Local) -> datetime:
    """Get current datetime based on specified localization"""
    currentTime: datetime

    if localization == TimeCoordinate.UTC:
        currentTime = datetime.datetime.utcnow()
    elif localization == TimeCoordinate.Local:
        currentTime = datetime.datetime.today()

    return currentTime


def main():
    isRunning: bool = True

    while isRunning:
        localStr: str = input("View UTC or local time? ")

        # Use local time if user input is invalid.
        localEnum = TimeCoordinate.Local

        # Convert str to TimeCoordinate
        if localStr.lower() == "local":
            localEnum = TimeCoordinate.Local
        elif localStr.lower() == "utc":
            localEnum = TimeCoordinate.UTC

        print("Current time is: " + str(getTime(localEnum)))


if __name__ == "__main__":
    main()
