#!/usr/bin/env python3

from datetime import datetime


def main():
    print("formatting_start")

    now = datetime.now()
    print(now.strftime("%a, %d, %B, %Y"))

    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))

    print(now.strftime("Current time is: %I:%M:%S:%p"))
    print(now.strftime("24-hour time is: %H:%M"))

if __name__ == "__main__":
    main()
