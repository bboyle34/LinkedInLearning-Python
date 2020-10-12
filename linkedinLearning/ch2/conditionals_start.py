#!/usr/bin/env python3


def main():
    print("conditionals_start")
    x, y = 100, 100

    if (x < y):
        st = "x is less than y"
    elif (x > y):
        st = "x is greater than y"
    else:
        st = "x is equal to y"

    print(st)

if __name__ == "__main__":
    main()
