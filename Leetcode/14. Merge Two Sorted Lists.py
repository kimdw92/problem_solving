# 연결 리스트 14 두 정렬 리스트의 병합
# 재귀

# 풀이1
# 비교 후 head 연결 리스트에 재귀로 쌓음
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:
            head = ListNode(l2.val)
            head.next = self.mergeTwoLists(l1, l2.next)
        else:
            head = ListNode(l1.val)
            head.next = self.mergeTwoLists(l1.next, l2)
        return head
