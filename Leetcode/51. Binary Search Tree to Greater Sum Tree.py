# 1038 이진 탐색 트리(BST)를 더 큰 수 합계 트리로
# 이진 트리
# 중위 순회(In-Order) 를 이용해서 오른쪽 -> 부모 -> 왼쪽으로 순회하면서 val 갱신
class Solution:
    val: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        # 오른쪽 -> 부모 -> 왼쪽 순서
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        return root
