from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen

    def dfs(self, currentNode, currentVal):
        if currentNode is None:
            return
        self.seen.add(currentVal)
        self.dfs(currentNode.left, currentVal * 2 + 1)
        self.dfs(currentNode.right, currentVal * 2 + 2)
