
def areAlmostEqual(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    diff = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff.append(i)
    if not diff:
        return True
    return len(diff) == 2 and s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]

print(areAlmostEqual("bank", "banka"))