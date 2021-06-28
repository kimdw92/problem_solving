# 108. 정렬된 배열의 이진 탐색 트리 변환
# 이진 탐색 트리(Binary Search Tree)
# BST는 탐색 시 시간 복잡도가 O(log n) 으로 매우 유리하다
# 이진 검색은 재귀, 분할 정복 구조로 구현
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        # 분할 정복으로 이진 검색
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])          
        return node
