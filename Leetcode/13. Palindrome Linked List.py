# 연결 리스트 13 팰린드롬 연결 리스트

# 풀이1: 리스트로 변환
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []
            
        if not head:
            return True
        
        node = head
        # 리스트로 변환
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True
      
# 풀이2: 데크로 최적화
# 동적배열에서 첫번째 값을 꺼내오면 shifting 이 일어나서 O(n) 시간복잡도가 발생한다. Deque는 이중 연결 리스트 구조로 O(1)이다.
def isPalindrome(self, head: ListNode) -> bool:
        # 데크 자료형 선언
        q: Deque = collections.deque()
            
        if not head:
            return True
        
        node = head
        # 리스트로 변환
        while node is not None:
            q.append(node.val)
            print(node.val)
            node = node.next
        
        # 팰린드롬 판별
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True
      
# 풀이3: 런너를 이용한 우아한 풀이
def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용한 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
            
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
