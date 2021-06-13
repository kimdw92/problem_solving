# 19 연결 리스트: 역순 연결 리스트 II

# My answer: 시작점 찾고, 반복 구조로 노드 뒤집기 24 ms	14.3 MB
def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 예외 처리
        if left == right:
            return head    
        # 시작점 찾기
        idx = 0
        left_node = ListNode(None)
        left_node.next = head
        start = left_node
        while True:
            if idx == left - 1:
                node = left_node.next
                idx += 1
                break
            left_node = left_node.next
            idx += 1           
        
        # 역순으로 바꾸기
        right_node = ListNode(None)
        rev_last = node
        while idx <= right+1:
            if idx > right:
                left_node.next = right_node
                rev_last.next = node
                break
            next, node.next = node.next, right_node
            right_node = node
            node = next
            
            idx += 1

        return start.next
      
# 풀이1: 좀더 깔끔한 풀이 24 ms	14.4 MB
def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        m, n = left, right
        # 예외 처리
        if not head or left == right:
            return head
        
        # 시작점 찾기
        start = left_node = ListNode(None)
        left_node.next = head
        
        for _ in range(m-1):
            left_node = left_node.next
        end = left_node.next    
        
        # 역순으로 바꾸기
        for _ in range(n-m):
            left_node.next, end.next, temp  = end.next, end.next.next, left_node.next
            left_node.next.next = temp
        
        return start.next
