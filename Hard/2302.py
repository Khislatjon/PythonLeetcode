from typing import List

def countSubarrays(nums: List[int], k: int) -> int:
    count = 0
    left = 0
    current_sum = 0
    for right in range(len(nums)):
        current_sum += nums[right]

        while left <= right and current_sum * (right - left + 1) >= k:
            current_sum -= nums[left]
            left += 1

        count += right - left + 1
    return count

print(countSubarrays([2, 1, 4, 3, 5], 20))
