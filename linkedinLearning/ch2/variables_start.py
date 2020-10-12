#!/usr/bin/env python3
def main():
    print("variables_start.py")
    f="abc"
    #print(f)
    #h = 1
    #t = 2
    #print(h + t)
    someFunction()
    print(f)

def someFunction():
    global f
    f="def"
    print(f)
    


if __name__ == "__main__":
    main()
