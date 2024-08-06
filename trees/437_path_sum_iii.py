from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # The idea behind this solution is to run DFS from every node in the tree with a sum starting from 0. At each call of the dfs
    # we add the current nodes value to the running sum and if it is equal to the target sum we increment the number of paths by 1.
    # This is a brute force solution and takes O(n^2) time.
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        num = 0

        def dfs(root, curr_sum):
            nonlocal num
            if not root:
                return
            curr_sum += root.val
            if curr_sum == targetSum:
                num += 1
            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)

        def iterate_tree(root):
            if not root:
                return
            dfs(root, 0)
            iterate_tree(root.left)
            iterate_tree(root.right)
        iterate_tree(root)
        return num
