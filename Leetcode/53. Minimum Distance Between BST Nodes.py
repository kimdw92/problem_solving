# 783 BST 노드 간 최소거리

# 중위순회(LNR)
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
            
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.result
