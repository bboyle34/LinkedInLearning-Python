#!/usr/bin/env python3




def main():
    print("files_start")
    #f = open("textfile.txt", "w+")
    #f = opent("textfile.txt", "a")
    f = open("textfile.txt", "r")
    #for i in range(10):
        #f.write("This is line " + str(i) + "\r\n")
    
    if f.mode == 'r':
        contents = f.read()
        print(contents)

    f.close




if __name__ == "__main__":
    main()
