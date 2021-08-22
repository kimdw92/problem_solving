# 19 Remove Nth Node From End of List
# Linked List
# Medium

# My answer 36 ms	14.2 MB
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = left = right = ListNode()
        start.next = head
        # initialize to have distance n between two pointer
        for _ in range(n):
            right = right.next
        
        while right and right.next:
            left, right = left.next, right.next
            
        left.next = left.next.next
            
        return start.next
            
