class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(i, sum):
            if sum == n:
                return True
            if sum > n or 3**i > n:
                return False
            if backtrack(i+1, sum + 3**i):
                return True
            return backtrack(i+1, sum)
        return backtrack(0, 0)