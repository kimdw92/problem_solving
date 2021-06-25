# 104 이진 트리의 최대 깊이
# BFS
def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0
        
        while queue:
            depth += 1
            # while 한바퀴가 depth 1개 이므로 모든 부모노드들의 자식들을 append 해야 함
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
            
        return depth
