from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minPrefixSum = 0
        maxPrefixSum = 0
        prefixSum = 0
        for num in nums:
            prefixSum += num
            minPrefixSum = min(minPrefixSum, prefixSum)
            maxPrefixSum = max(maxPrefixSum, prefixSum)
        return maxPrefixSum - minPrefixSum
