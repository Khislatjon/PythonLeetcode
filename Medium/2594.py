from cmath import sqrt
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def countRepair(time):
            count = 0
            for r in ranks:
                count += int(sqrt(time / r))
            return count >= cars

        l, r = 0, ranks[0] * cars * cars
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if countRepair(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res