from typing import List

def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    odd = 0
    for a in arr:
        if a % 2 != 0:
            odd += 1
        else:
            odd = 0
        if odd == 3:
            return True
    return False