#!/usr/bin/env python3

def main():
    game = 0
    rows, cols = 7, 6
    board = [["0" for x in range(rows)] for y in range(cols)]
    while game != 1:
        #display board
        printBoard(board)
        #first player goes
        move(board, "1", "X")
        #check if player won
        gameCheck(board)
        #display board
        printBoard(board)
        #second player goes
        move(board, "2", "Y")
        #check if player won
        gameCheck(board)
        


#funciton to print the board
def printBoard(board):
    print()
    print("___________________________________________")
    print()
    tank = 0
    for i in range(len(board)):
        for h in range(len(board[i])):
            if i == 0:
                if h == 0:
                    print("| ", end = " ")   
                print(h, end = " ")
                print(" | ", end = " ")
                tank = 1
            if h == len(board) and tank == 1:
                print()
                print("___________________________________________") 
                print()
        tank = 0
        print("| ", end = " ")
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
            print(" | " , end = " ")
        print()
        if i != len(board) - 1:
            print()
    print("___________________________________________")
    print()
 
#function to input player x move
def move(board, player, mark):
    smart = True
    while (smart):
        #try:
        move = int(input("Your move, player" + player + ": "))
        #smart = False
        #except:
        #print("Please input a number")
        if move < 0 or move > 6:
            print("Please select a move 1-6")   
        else:
            smart = False
        #dumb = False
        #while not (dumb):
            #if spot is not == 0, replce 0 with X
        if not (smart):
            for i in range(len(board)):
                #try:
                if board[5 - i][move] == "0":
                    board[5 - i][move] = mark
                    #dumb = True
                    smart = False
                    break
                if i == 5:
                    print("Column limit reached")
                    smart = True
                #except:
            
                
#funciton to check if game has been won yet
#check if 4 across, 4 vertical, 4 diagonal right, 4 diagonal left
def gameCheck(board):
    #have a counter that increments when there are two of the same tiles next to each other
    #check each [i][j] for same tiles to the right, left, up, down, and horizontal
    #right left [i][j+-1]
    #up down [i+-1][j]
    #horizontal [i-1][j-1] [i-1][j+1] [i+1][j+1] [i+1][j-1]
    consec = 0
    full = 0
    while (full < 42 and consec != 4):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == 0 and j == 0:
                    #only check right, down, and rdown
                elif i == 0 and j > 0 or j < 6
                    #only check down, left, right, ldown, and rdown
                elif i == 0 and j == 6:
                    #only check right, down, and ldown
                elif i > 0 and i < 5 and j == 0:
                    #only check left, up, down, rup, and rdown
                elif i > 0 and i < 5 and j > 0 and j < 6:
                    #only check up, down, left, right, lup, rup, ldown, and rdown
                elif i > 0 and i < 5 and j == 6:
                    #only check left, up, down, lup, and ldown
                elif i == 5 and j == 0:
                    #only check right, down, rup
                elif i == 5 and j > 0 and j < 6:
                    #only check left, right, up, lup, and rup
                elif i == 5 and j == 6:
                    #only check left, up and lup
                else:
                    print("Idk how you got here")
                    
                full = full + 1
                print(full)
            


if __name__ == "__main__":
    main()
