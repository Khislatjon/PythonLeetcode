from typing import List
def partitionLabels(self, s: str) -> List[int]:
    lastIndex = {}
    for i, ch in enumerate(s):
        lastIndex[ch] = i

    res = []
    size, end = 0, 0
    for i, ch in enumerate(s):
        size += 1
        end = max(end, lastIndex[ch])
        if i == end:
            res.append(size)
            size = 0
    return res