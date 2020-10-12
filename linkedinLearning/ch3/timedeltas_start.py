#!/usr/bin/env python3

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
    print("timedeltas_start")
    print(timedelta(days=365, hours=5, minutes=1))
    
    now = datetime.now()
    print("Today is: " + str(now))
    print("One year from now it will be " + str(now + timedelta(days=365)))

    print("In 2 days and 3 weeks it will be " + str(now + timedelta(days=2, weeks=3)))

    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d %y")
    print("One week ago it was " + s)

    today = date.today()
    afd = date(today.year, 4, 1)
    if afd < today:
        print("April fool's day went by %d days ago" % ((today-afd).days))
        afd = afd.replace(year = today.year+1)
    timeToAfd = afd-today
    print("It's just time to", timeToAfd.days, "days until April fool's day")



if __name__ == "__main__":
    main()
