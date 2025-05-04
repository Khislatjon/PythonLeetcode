def countSymmetricIntegers(low: int, high: int) -> int:
    def isSymmetric(n) -> bool:
        s = str(n)
        l = len(s)
        if l % 2 == 1:
            return False
        a, b = s[:l//2], s[l//2:]
        return sum(int(i) for i in a) == sum(int(i) for i in b)
    count = 0
    for i in range(low, high + 1):
        if isSymmetric(i):
            count += 1
    return count