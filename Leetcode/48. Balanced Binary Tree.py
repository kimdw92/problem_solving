# 110 균형 이진 트리
# easy

# My answer
# DFS 재귀 탐색
class Solution:
    result = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        def dfs(root):
            if root is None:
                return 0
            left_h = dfs(root.left)
            right_h = dfs(root.right)
            if abs(left_h - right_h) > 1:
                self.result = False
            
            return max(left_h, right_h) + 1
        
        dfs(root)
        return self.result
