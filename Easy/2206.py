from collections import defaultdict
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums) / 2
        dict = defaultdict(int)

        for i in nums:
           dict[i] += 1
        for key, val in dict.items():
            if val % n != 0:
                return False
        return True