#!/usr/bin/env python3


def main():
    print("test")
    

    for i in range(10):
        ans = input("continue? (y/n) ")
        if ans == "y":
            print(i)
        else:
            i = i-1
            print(i)

if __name__ == "__main__":
    main()
