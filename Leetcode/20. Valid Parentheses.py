# 스택 20. 유효한 괄호

# 스택 일치 여부 판별 36 ms	14.1 MB
def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        for char in s:
            if char not in table:
                stack.append(char)
            elif stack == [] or table[char] != stack.pop():
                return False
            
        return len(stack) == 0
