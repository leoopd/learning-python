# 2133. Check if Every Row and Column Contains All Numbers

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        digits = list(range(1, len(matrix)+1))
        matrix2 = []
        for row in matrix:
            for digit in digits:
                if digit not in row:
                    return False
        
        # Transposing the matrix
        for i in range(len(matrix)):
            tmp = []
            for j in range(len(matrix)):
                tmp.append(matrix[j][i])
            matrix2.append(tmp)
        
        for column in matrix2:
            for digit in digits:
                if digit not in column:
                    return False
        
        return True
