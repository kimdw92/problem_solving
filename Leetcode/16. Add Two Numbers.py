# 연결 리스트 16: 두 수의 덧셈

# My answer: sum 연결 리스트 생성 76 ms	14.1 MB
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = ListNode(0)
        answer = sum
        over = 0
        while l1 or l2 or over:
            sum.next = ListNode(0)
            sum = sum.next
            # l1, l2의 길이가 다를 경우 0으로 채우며 진행
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
                
            # 앞에서 넘어온 over(1 or 0)와 덧셈
            sum_temp = l1.val + l2.val + over            
            over, val = divmod(sum_temp, 10)
            sum.val = val
            l1, l2 = l1.next, l2.next
                        
        return answer.next
      
      
 
# 풀이2: 전가산기
# root.next 리턴 (맨앞에 하나 빼기)
# 몫과 나머지 계산: carry, val = divmod(sum + carry, 10)
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # 몫과 나머지 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
            
        return root.next
      
# 풀이1: 리스트로 바꿔서 푸는 무식한 방법
# 리스트를 합쳐서 숫자로 바꾸는 방법 int(''.join(str(e) for e in a))
class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
    
    # 연결 리스트를 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: list = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    # 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
            
        return node
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        return self.toReversedLinkedList(str(resultStr))
