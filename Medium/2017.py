from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefixSum1, prefixSum2 = grid[0].copy(), grid[1].copy()
        for i in range(1, n):
            prefixSum1[i] += prefixSum1[i-1]
            prefixSum2[i] += prefixSum2[i-1]

        res = float("inf")
        for i in range(n):
            top = prefixSum1[-1] - prefixSum1[i]
            bottom = prefixSum2[i-1] if i > 0 else 0
            res = min(res, max(top, bottom))
        return res