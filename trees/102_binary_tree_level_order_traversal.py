# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Need to use a queue to keep track of the visited levels, just run a regular BFS O(n) time O(n/2) extra space
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        output = []
        while q:
            levellen = len(q)
            cur = []
            for i in range(levellen):
                node = q.popleft()
                if node:
                    cur.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if cur:
                output.append(cur)
        return output
