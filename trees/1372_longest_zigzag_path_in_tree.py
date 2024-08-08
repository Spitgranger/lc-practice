from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # this solution runs a dfs on every single node and checks if the path found is greater than the current zigzag path.
    # it currently TLEs as O(n^2)
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ret_len = 0

        def dfs(root, direction, path_length):
            if not root:
                return path_length
            if direction == 1:
                return dfs(root.left, 0, path_length + 1)
            else:
                return dfs(root.right, 1, path_length + 1)

        def iterate_tree(root):
            if not root:
                return
            nonlocal ret_len
            ret_len = max(ret_len, dfs(root, 0, 0), dfs(root, 1, 0))
            iterate_tree(root.left)
            iterate_tree(root.right)
        iterate_tree(root)
        return ret_len - 1
