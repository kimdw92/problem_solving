# 트리 226. 이진 트리 반전

# 풀이1 재귀
def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        
# 풀이2 BFS
def invertTree(self, root: TreeNode) -> TreeNode:
        q = collections.deque([root])     
        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)  
            
        return root
