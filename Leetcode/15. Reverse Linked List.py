# 연결 리스트 15: 역순 연결 리스트

# My answer: 반복분으로 rev 생성 52 ms	16.4 MB
def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        next_node = None
        while head is not None:
            rev = ListNode(head.val)
            rev.next = next_node
            next_node = rev
            head = head.next
        return rev
      
# 풀이1: 반복 구조로 뒤집기... 직관적으로 이해하기 어려움 68 ms	15.6 MB
def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
      
# 풀이2: 재귀 구조로 뒤집기... 219p (이해 포기)      
