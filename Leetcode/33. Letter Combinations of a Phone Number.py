# 17. 전화번호 문자조합

# dfs, 모든 조합 탐색. 
 def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
           '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        if not digits:
            return []
        
        def dfs(index, path):
          # 끝까지 탐색하면 백트래킹
            if index == len(digits):
                result.append(path)
                return
            
            for char in dic[digits[index]]:
              # 다음 문자열 반복
                dfs(index+1, path+char)
                    
        dfs(0, '')
        return result
