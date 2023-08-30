from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution is O(n) since we are traversing through all the elements in the tree
def isBalanced(root: Optional[TreeNode]) -> bool:
    flag = True
    def dfs(root):
        nonlocal flag
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        if abs(left - right) > 1:
            flag = False
        return 1 + max(left, right)
    dfs(root)
    return flag