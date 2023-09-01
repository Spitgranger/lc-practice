def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    leftarr = []
    rightarr = []
    def search(root, node, arr):
        if not root:
            return
        if node.val == root.val:
            arr.append(root)
            return
        arr.append(root)
        if root.val < node.val:
            search(root.right, node, arr)
        elif root.val > node.val:
            search(root.left, node, arr)
    search(root, p, leftarr)
    search(root, q, rightarr)
    i = 0
    j = 0
    while i < len(leftarr) and j < len(rightarr):
        if i + 1 == len(leftarr) and leftarr[i] == rightarr[j]:
            return leftarr[i]
        elif j + 1 == len(rightarr) and leftarr[i] == rightarr[j]:
            return leftarr[j]
        if leftarr[i].val != rightarr[j].val:
            return leftarr[i - 1]
        i += 1
        j += 1

# Solution using the propertities of binary search tree, o(ln(n)) and O(H) SPACE
def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(tree, p, q):
        if tree.val > p.val and tree.val > q.val:
            return dfs(tree.left, p, q)
        elif tree.val < p.val and tree.val < q.val:
            return dfs(tree.right, p, q)
        else:
            return tree
    return dfs(root, p, q)
