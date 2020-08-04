from itertools import *
from copy import copy


def is_distinct(list):
    '''
    checks if all elements in a list are distinct
    (ignores 0s)
    '''
    used = []
    for i in list:
        if i == 0:
            continue
        if i in used:
            return False
        used.append(i)
    return True


def is_valid(brd):
    '''Checks if a 9x9 Sudoku is valid.'''
    for i in range(9):
        row = [brd[i][0], brd[i][1], brd[i][2], brd[i][3], brd[i]
               [4], brd[i][5], brd[i][6], brd[i][7], brd[i][8]]
        if not is_distinct(row):
            return False
        col = [brd[i][0], brd[i][1], brd[i][2], brd[i][3], brd[i]
               [4], brd[i][5], brd[i][6], brd[i][7], brd[i][8]]
        if not is_distinct(col):
            return False
    return True


def solve(brd, empties):
    '''
      Solves Sudoku puzzle
      brd is the board
      empties is the number of empty cells
    '''

    if empties == 0:
        # If there are no more empty spaces, return the filled board
        return is_valid(brd)
    for row, col in product(range(9), repeat=2):
        # Run through every cell
        cell = brd[row][col]
        if cell != 0:
            # If the cell is not empty, go to the next one
            continue
        brd2 = copy(brd)
        for test in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            brd2[row][col] = test
            if is_valid(brd2) and solve(brd2, empties-1):
                return True
            brd2[row][col] = 0
    return False


Board = [[5, 3, 0, 0, 7, 0, 0, 0, 0, ],
         [6, 0, 0, 1, 9, 5, 0, 0, 0, ],
         [0, 9, 8, 0, 0, 0, 0, 6, 0, ],
         [8, 0, 0, 0, 0, 0, 0, 0, 3, ],
         [4, 0, 0, 0, 6, 0, 0, 0, 1, ],
         [7, 0, 0, 8, 0, 3, 0, 0, 6, ],
         [0, 6, 0, 0, 0, 0, 2, 8, 0, ],
         [0, 0, 0, 4, 1, 9, 0, 0, 5, ],
         [0, 0, 0, 0, 8, 0, 0, 7, 9, ],
         ]

HardestSudokuPuzzle = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

solve(HardestSudokuPuzzle, 81 - 21)


for row in HardestSudokuPuzzle:  # Prints a solution
    print(row)
