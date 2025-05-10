from typing import List

def minSum(nums1: List[int], nums2: List[int]) -> int:
    zeroC1 = zeroC2 = 0
    sum1 = sum2 = 0
    for num1 in nums1:
        sum1 += num1
        if num1 == 0:
            zeroC1 += 1
            sum1 += 1
    for num2 in nums2:
        sum2 += num2
        if num2 == 0:
            zeroC2 += 1
            sum2 += 1
    if sum2 > sum1 and zeroC1 == 0:
        return -1
    if sum1 > sum2 and zeroC2 == 0:
        return -1
    return max(sum1, sum2)