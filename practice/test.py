#!/usr/bin/env python3


def main():
    print("test")
    list = [2, 4, 6, 8]                             
    while 1 > 0:    
        ans = int(input("Choose a number: "))
        turn = 0
        count = 0
        for i in list:
            if i > ans:
                list.insert(count, ans)
                turn += 1
                break
            count += 1
        if turn == 0:
            list.append(ans)
        
        print(list)
if __name__ == "__main__":
    main()
