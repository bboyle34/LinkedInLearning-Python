#!/usr/bin/env python3


def main():
    print("connectNotes")

    print()

    rows = 6
    cols = 7
    board = [[0 for x in range(rows)] for y in range(cols)]

    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print()

    


if __name__ == "__main__":
    main()
