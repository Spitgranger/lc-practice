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

    # Working solution O(n) runtime run a dfs on the tree at each node, keeping track of the current left and right paths.
    # at each level if we go right that means we went left before, so increment that path, if we go left that means we went right
    # before so increment the right path and reset
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ret_val = 0

        def dfs(root, left, right):
            nonlocal ret_val
            if not root:
                return
            ret_val = max(ret_val, left, right)
            dfs(root.right, 0, left + 1)
            dfs(root.left, right + 1, 0)
        dfs(root, 0, 0)
        return ret_val
