class Solution:
    def nodeSum(self, root, l, r):
        
        def dfs(node):
            if node is None:
                return 0
            if node.data < l:
                return dfs(node.right)
            elif node.data > r:
                return dfs(node.left)
            else:
                return dfs(node.left) + node.data + dfs(node.right)
        
        return dfs(root)
