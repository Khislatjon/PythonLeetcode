class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        whites = 0
        minW = float("inf")
        for r in range(len(blocks)):
            if blocks[r] == "W":
                whites += 1
            if r - l + 1 == k:
                minW = min(minW, whites)
                if blocks[l] == "W":
                    whites -= 1
                l += 1
        return minW
