from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lcaDeepestLeaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(node, depth):
        if not node:
            return None, depth

        leftLCA, leftDepth = dfs(node.left, depth + 1)
        rightLCA, rightDepth = dfs(node.right, depth + 1)

        if leftDepth > rightDepth:
            return leftLCA, leftDepth
        elif rightDepth > leftDepth:
            return rightLCA, rightDepth
        else:
            return node, leftDepth

    lca, _ = dfs(root, 0)
    return lca