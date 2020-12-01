#!/usr/bin/env python3
#given a list of numbers, this will print out all combinations of the corresponding letters
#2 = abc
#3 = def
#4 = ghi
#5 = jkl
#7 = mno
#7 = pqrs
#8 = tuv
#9 = wxyz

def main():
    print("licenseRead")
    print()

    atlas = [['A', 'B', 'C'], ['D', 'E','F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
    num = 2

    for i in range(len(atlas)):
        for j in range(len(atlas[i])):
            if j == 0:
                print(str(num) + ". ", end = " ")
            print(atlas[i][j], end = " ")
        print()
        num = num + 1


    print()
    print()
    license = int(input("Please input your license number: "))
    licenseList = list(map(int, str(license)))
    answer = [len(licenseList)][]
    for x in range(len(licenseList)):
        num = 2
        while num < 10:
            for i in range(len(atlas)):
                for j in range(len(atlas[i])):
                    if  num == licenseList[x]:
                        answer.append(atlas[i][j])
                   #it was at this moment i realized how goddam hard this is going to be 
                    #i need a whiteboard
            num = num + 1

    for i in range(len(answer)):
        print(answer[i], end = "")
    print()





if __name__ == "__main__":
    main()
