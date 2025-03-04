from typing import List
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        merged = []
        while p1 < n1 and p2 < n2:
            id1, val1 = nums1[p1]
            id2, val2 = nums2[p2]
            if id1 == id2:
                merged.append([id1, val1 + val2])
                p1 += 1
                p2 += 1
            elif id1 < id2:
                merged.append([id1, val1])
                p1 += 1
            else:
                merged.append([id2, val2])
                p2 += 1
        while p1 < n1:
            merged.append(nums1[p1])
            p1 += 1
        while p2 < n2:
            merged.append(nums2[p2])
            p2 += 1
        return merged
