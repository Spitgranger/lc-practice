# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Solution is O(n) time. Run dfs on the tree and keep track of the current maximum in the path. If the current value is greater than the maximum,
# it must be good. Therefore increment the number of good nodes. O(h) extra space for the call stack.
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, maximum):
            nonlocal count
            if not root:
                return
            if root.val >= maximum:
                maximum = root.val
                count += 1
            dfs(root.right, maximum)
            dfs(root.left, maximum)
        dfs(root, -100000)
        return count