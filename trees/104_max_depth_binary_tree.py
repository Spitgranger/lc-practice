from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def maxDepth(root: Optional[TreeNode]) -> int:
    def dfs(root, cur_height):
        if root == None:
            return cur_height
        cur_height += 1
        return max(dfs(root.right, cur_height), dfs(root.left, cur_height))
    return dfs(root, 0)
