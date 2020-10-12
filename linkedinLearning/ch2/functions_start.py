#!/usr/bin/env python3


def main():
    print("functions_start")
    #func1()
    #prin://www.linkedin.com/in/brendan-boyle-b78175130/t(func1())
    
    #func2(10, 20)
    #print(func2(10, 20))
    #print(cube(3))

    print(power(2))
    print(power(2, 3))
    print(power(x=3, num=2))
    print(multiadd(4, 5, 10, 4))

def func1():
    print("I am a function")

def func2(arg1, arg2):
    print(arg1, " ", arg2)

def cube(x):
    return x*x*x

def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

def multiadd(*args):
    result = 0
    for x in args:
        result = result + x
    return result
    


if __name__ == "__main__":
    main()
