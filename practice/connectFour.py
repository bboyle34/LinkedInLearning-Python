#!/usr/bin/env python3

def main():
    game = 0
    rows, cols = 7, 6
    board = [[0 for x in range(rows)] for y in range(cols)]
    while game != 1:
        #display board
        printBoard(board)
        #first player goes
        xMove(board)
        #check if player won
        gameCheck(board)
        #display board
        printBoard(board)
        #second player goes
        yMove(board)
        #check if player won
        gameCheck(board)
        


#funciton to print the board
def printBoard(board):
    print()
    print("___________________________________________")
    print()
    for i in range(len(board)):
        print("| ", end = " ")
        for h in range(len(board[i])):
            if i == 0:
                print(h, end = " ")
                print(" | ", end = " ")
        
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
            print(" | " , end = " ")
        print()
        if i != len(board) - 1:
            print()
    print("___________________________________________")
    print()
 
#function to input player x move
#this will include gravity
def xMove(board):
    move = input("Your move, player 1. ")
        

#function to input player y move
def yMove(board):
    move = input("Your move, player 2")

#funciton to check if game has been won yet
#check if 4 across, 4 vertical, 4 diagonal right, 4 diagonal left
def gameCheck(board):
    print("I have no clue if anyone is winning")


if __name__ == "__main__":
    main()
