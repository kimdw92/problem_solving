# 241. 괄호를 삽입하는 여러가지 방법
# 분할 정복
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results
                    
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        
        for index, value in enumerate(expression):
            # 분할
            if value in '-+*':
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])
                
                # 정복
                results.extend(compute(left, right, value))
                
        return results
