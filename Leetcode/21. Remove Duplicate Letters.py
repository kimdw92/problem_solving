# 스택 큐: 중복 문자 제거

# 스택을 이용한 문자 제거
def removeDuplicateLetters(self, s: str) -> str:
        # stack에 쌓으면서, 똑같은 문자가 남아있고 다음 문자가 더 작다면 삭제
        counter, stack = collections.Counter(s), []
        
        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            
            while (stack != []) and (stack[-1] > char) and (counter[stack[-1]]) > 0:
                stack.pop()
            stack.append(char)
        return ''.join(stack)
