def countGoodNumbers(n: int) -> int:
    mod = 10 ** 9 + 7
    def helper(x: int, n: int) -> int:
        res = 1
        while n > 0:
            if n % 2:
                res = (x * res) % mod  # eventually gets here
            n = n // 2
            x = (x * x) % mod
        return res
    return helper(5, (n + 1) // 2) * helper(4, n // 2) % mod