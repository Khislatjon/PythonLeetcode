from collections import Counter

def canConstruct(s: str, k: int) -> bool:
    if k > len(s):
        return False

    count = Counter(s)
    odd = 0
    for ct in count.values():
        odd += ct % 2
    return odd <= k


result = canConstruct("annabelle", 2)
print(result)
