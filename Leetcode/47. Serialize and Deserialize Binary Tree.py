# 297.  Serialize and Deserialize Binary Tree
# Hard
# 이진 트리 직렬화 & 역직렬화
# bfs이용

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        q = collections.deque([root])
        ser = []
        while q:
            node = q.popleft()  
            if node:
                q.append(node.left)
                q.append(node.right)
                ser.append(str(node.val))
            else:
                ser.append('#')
        
        return ' '.join(ser)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        nodes = data.split()
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        idx = 1
        while q:
            node = q.popleft()
            if nodes[idx] != '#':
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx += 1
            if nodes[idx] != '#':
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx += 1
        return root
            
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
