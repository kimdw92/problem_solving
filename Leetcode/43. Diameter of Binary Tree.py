# 543. 이진 트리의 직경
# DFS
# 어떤 노드의 직경 = left에서 leaf까지의 길이 + right에서 leaf까지의 길이 + 2
class Solution: 
    # 중첩함수 dfs에서 재할당이 이루어지면 참조가 바뀌기 때문에 클래스 변수로 선언
    longest : int = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:    
        def dfs(node):
            if node is None:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
