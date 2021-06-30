# 105 전위, 중위 순회 결과로 이진 트리 구축
# 전위순회 preorder traversal
# 중위순회 inorder traversal
# 전위순회의 첫번째 값은 루트이고, 이 값은 중위순회를 left와 right로 가르는 분기점이다.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))
            
            # 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])
            
            return node
