from typing import List

# def findNumbers(nums: List[int]) -> int:
#     evenCount = 0
#     for num in nums:
#         if len(str(num)) % 2 == 0:
#             evenCount += 1
#     return evenCount

def findNumbers(nums: List[int]) -> int:
    def isEvenCount(num):
        count = 0
        while num > 0:
            count += 1
            num //= 10
        return count % 2 == 0

    evenCount = 0
    for num in nums:
        if isEvenCount(num):
            evenCount += 1
    return evenCount

print(findNumbers([12, 34, 232, 10]))