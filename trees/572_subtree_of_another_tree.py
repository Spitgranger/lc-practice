from typing import Optional
# Time complexity is O(n*m) the size of both trees multiplied by each other
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def equal(tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 and tree2 or tree1 and not tree2:
            return False
        if tree1.val != tree2.val:
            return False
        return equal(tree1.left, tree2.left) and equal(tree1.right, tree2.right)
    def dfs(r):
        if not r:
            return False
        if equal(r, subRoot):
            return True
        return dfs(r.right) or dfs(r.left)
    return dfs(root)
