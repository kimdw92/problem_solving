# 240 2D 행렬 검색2

# 풀이1:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        answer = False
        m, n = 0, len(matrix[0])-1
        
        while m >= 0 and m < len(matrix) and n >= 0 and n < len(matrix[0]):
            if matrix[m][n] < target:
                m += 1
            elif matrix[m][n] > target:
                n -= 1
            else:
                return True
        return answer
    
# 풀이2: Pythonic way
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)
