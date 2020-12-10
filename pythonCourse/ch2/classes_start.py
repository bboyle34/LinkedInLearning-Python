#!/usr/bin/env python3

class myClass():
    def method1(self):
        print("myClass method1")
    
    def method2(self, someString):
        print("myClass method2 " + someString)

    def method3(self):
        print("myClass method3")

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherClass method2 " + someString)


def main():
    print("classes_start")
    
    c = myClass()
    c.method1()
    c.method2("this is a string")
    c.method3() 
    
    a = anotherClass()
    a.method1()
    a.method2("this is another string")
    a.method3()

if __name__ == "__main__":
    main()
