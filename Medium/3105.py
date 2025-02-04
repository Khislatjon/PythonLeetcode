from typing import List

def longestMonotonicSubarray(nums: List[int]) -> int:
    n = len(nums)
    inCounter = 1
    deCounter = 1
    maxCount = 1
    for i in range(1, n):
        if nums[i-1] < nums[i]:
            inCounter += 1
            deCounter = 1
        elif nums[i-1] > nums[i]:
            deCounter += 1
            inCounter = 1
        else:
            inCounter = 1
            deCounter = 1
        maxCount = max(maxCount, inCounter, deCounter)
    return maxCount

result = longestMonotonicSubarray([3,2,1,2,3,4])
print(result)