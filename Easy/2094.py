from typing import List

def findEvenNumbers(digits: List[int]) -> List[int]:
    nums = set()
    n = len(digits)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or i == k or j == k:
                    continue
                num = digits[i]*100 + digits[j]*10 + digits[k]
                if num >= 100 and num % 2 == 0:
                    nums.add(num)
    return sorted(list(nums))

print(findEvenNumbers([3, 1, 6, 8]))