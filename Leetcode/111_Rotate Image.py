# 48 Rotate Image

# My answer
import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) # 행 길이 계산
        m = len(matrix[0]) # 열 길이 계산
        matrix2 = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(m):          
                matrix[j][n-i-1] = matrix2[i][j]
