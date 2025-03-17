from typing import List
import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n) -> bool:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return n > 1

        primes = []
        for i in range(left, right + 1):
            if i % 2 == 0 and i > 2:
                continue
            if isPrime(i):
                # returning [2,3] or [3,5] cases
                if primes and i <= primes[-1] + 2:
                    return [primes[-1], i]
                primes.append(i)

        if len(primes) < 2:
            return [-1, -1]

        result = [-1, -1]
        minDiff = 1e6
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < minDiff:
                minDiff = primes[i] - primes[i - 1]
                result = [primes[i - 1], primes[i]]

        return result


result = Solution().closestPrimes(4, 6)
print(result)

