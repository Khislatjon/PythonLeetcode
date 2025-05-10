from typing import List

def buildArray(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n):
        nums[i] += 1000 * (nums[nums[i]] % 1000)
    for i in range(n):
        nums[i] //= 1000
    return nums