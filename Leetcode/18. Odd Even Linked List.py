# 연결리스트 18: 홀짝 연결리스트
# odds 연결리스트, evens 연결리스트 만든 후 마지막에 연결

# My answer: 반복문
def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        evens = head
        odds =  head.next
        odd_root = odds
        even_root = evens
        
        while evens or odds:   
            if evens.next is None or odds.next is None:
                break       
            if evens and evens.next:
                evens.next = evens.next.next
                evens = evens.next
            if odds and odds.next:              
                odds.next = odds.next.next
                odds = odds.next
        evens.next = odd_root
       
        return even_root
      
# 풀이1 반복문, 좀더 깔끔한
def oddEvenList(self, head: ListNode) -> ListNode:
        # 예외 처리
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
            
        odd.next = even_head
        return head
