def countAndSay(n: int) -> str:
    def helper(n: int) -> str:
        if n == 1: return "1"
        return rle(helper(n - 1))

    def rle(s: str) -> str:
        count = 1
        result = ""
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                result += str(count) + s[i - 1]
                count = 1
        result += str(count) + s[-1]
        return result

    return helper(n)

print(countAndSay(5))