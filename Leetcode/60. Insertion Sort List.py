# 연결리스트에서 삽입정렬 구현
# 147 삽입 정렬 리스트

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
                
            cur.next, head.next, head = head, cur.next, head.next
            
            # 필요한 경우에만 cur 포인터가 되돌아가도록
            if head and cur.val > head.val:
                cur = parent
        return parent.next
