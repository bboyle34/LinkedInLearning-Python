#!/usr/bin/env python3
import calendar

def main():
    print("test")
    
    c = calendar.TextCalendar(calendar.SUNDAY)
    st = c.formatmonth(2020, 11, 0, 0)
    print(st)
    

if __name__ == "__main__":
    main()
