# This soluvtion is O(n) runtime and requires O(h) height of tree extra space for the call stackgi
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(root):
        if root == None:
            return
        dfs(root.left)
        dfs(root.right)
        root.left, root.right = root.right, root.left
    dfs(root)
    return root