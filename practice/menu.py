#!/usr/bin/env python3

from random import randint
import calendar
from datetime import date

#this is a menu that has a lot of useful options
#most if not all options are me testing my python skills

def rng():
    #generate 10 random distinct numbers until the user is satisfied or until the array is full with 100 numbers
    #lets add the numbers to the list in order
    list = []
    x = 0
    while x < 1:
        if len(list) > 99:
            print("the array is full of 100 numbers")
            print(list)
            break
        y = 0
        while y < 10:
            turn = 0
            count = 0
            num = randint(0, 100)
            if num in list:
                print("number exists, trying again...")
                
            else:
                print(num)
                for i in list:
                    if i > num:
                        list.insert(count, num)
                        turn += 1
                        break
                    count += 1
                if turn == 0:
                    list.append(num)
                y+= 1                

        ans = input("Do you wish to continue? (y/n)")
        if ans == "n":
            x = x + 1
            print(list)

def cal():
    c = calendar.TextCalendar(calendar.SUNDAY)
    today = date.today()
    st = c.formatmonth(2020, today.month, 0, 0)
    print(st)



def main():
    print("rng")
    
    dec = 0
    while dec < 1:
        print("1. (R)NG Machine \n2. (C)alendar Print \n3. (Q)uit")
        choice = input("what would you like to do? ")
        if choice == "R" or choice == "r" or choice == "1":
            rng()
        elif choice == "C" or choice == "c" or choice == "2":
            cal()
        elif choice == "Q" or choice == "q" or choice == "3":
            dec += 1
            break
        else:
            print("Please select a valid option")

    print("Shutting down...")        


if __name__ == "__main__":
    main()

     
