from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# DFS Solution keeping track of the level. For each dfs, if the current level is equal to the length of the output,
# append it to the output array. This solution gives preference to the right nodes as we run dfs at each level starting
# with the right child first.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        level = 0
        def dfs(node, level):
            if not node:
                return
            if level == len(output):
                output.append(node.val)
            level += 1
            dfs(node.right, level)
            dfs(node.left, level)
        dfs(root, 0)
        return output