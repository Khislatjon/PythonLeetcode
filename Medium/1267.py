from typing import List

def countServers(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    rowCount = [0] * rows
    colCount = [0] * cols

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                rowCount[r] += 1
                colCount[c] += 1
    res = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and max(rowCount[r], colCount[c]) > 1:
                res += 1
    return res
