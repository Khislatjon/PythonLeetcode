from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    zeroInFirstRow, zeroInFirstCol = False, False

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                if i == 0: zeroInFirstRow = True;
                if j == 0: zeroInFirstCol = True;
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if zeroInFirstRow:
        for j in range(cols):
            matrix[0][j] = 0
    if zeroInFirstCol:
        for i in range(rows):
            matrix[i][0] = 0