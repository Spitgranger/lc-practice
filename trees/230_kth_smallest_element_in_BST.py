from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# O(n) time O(n) extra space inorder traversal and return the k - 1 element in the array constructed. as inorder traversal
# of BST yields an array that in strictly increasing
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            array.append(node.val)
            dfs(node.right)
        dfs(root)
        return array[k-1]