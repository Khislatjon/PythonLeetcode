class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        def dfs(root, maxVal):
            nonlocal total
            if not root:
                return
            if root.val >= maxVal:
                total += 1
                maxVal = root.val
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        dfs(root, root.val)
        return total