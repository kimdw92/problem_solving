# 연결 리스트17: 페어의 노드 스왑

# My answer: 반복 구조로 스왑
def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        
        prev = ListNode()
        prev.next = node = head
        head = head.next
        while node is not None:
            prev.next = node
            next = node.next
            if next is None:
                break
            node.next, next.next, prev.next = next.next, node, next   
            prev = node
            node = node.next
        return head

# 풀이1: 반복 구조로 스왑
def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a(head)르 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head
            
            # prev가 b를 가리키도록 할당
            prev.next = b
            
            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next
      
# 풀이2: 재귀 구조로 스왑... 231p 잘 이해 안됨
