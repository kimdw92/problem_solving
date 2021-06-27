# 트리 687. 가장 긴 동일값의 경로
# 이진트리
# 상태값 거리 계산 DFS
class Solution:
    longest: int = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        def dfs(node: TreeNode):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
                
            
            self.longest = max(self.longest, left + right)
            return max(left, right)
        
        
        dfs(root)
        
        return self.longest
