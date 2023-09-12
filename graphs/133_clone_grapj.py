"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Runtime complexity of O(V + E) where V is the number of vertices and E is the number of edges
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(root):
            if root and root.val not in visited:
                ret = Node()
                ret.val = root.val
                visited.update({root: ret})
                for neighbor in root.neighbors:
                    if neighbor and neighbor not in visited:
                        ret.neighbors.append(dfs(neighbor))
                    else:
                        ret.neighbors.append(visited.get(neighbor))
                return ret

        return dfs(node)