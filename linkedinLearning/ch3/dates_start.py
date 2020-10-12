#!/usr/bin/env python3

from datetime import date
from datetime import time
from datetime import datetime

def main():
    print("dates_start")
    today = date.today()
    #print("Today's date is", today)    
    
    #print("Date components:", today.day, today.month, today.year)

    #print("Today's weeday # is:", today.weekday())
    #days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    #print("which is a:", days[today.weekday()])

    today = datetime.now()
    print(today)
    t = datetime.time(datetime.now())
    print(t)
    



if __name__ == "__main__":
    main()
