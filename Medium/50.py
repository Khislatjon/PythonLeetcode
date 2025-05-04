def myPow(x: float, n: int) -> float:
    if x == 0 or x == 1:
        return x

    def helper(x, n) -> float:
        if n == 0: return 1
        res = helper(x, n // 2)
        res = res * res
        return x * res if n % 2 else res

    res = helper(x, abs(n))
    return res if n >= 0 else 1 / res