# 2133. Check if Every Row and Column Contains All Numbers

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        digits = list(range(1, len(matrix)+1))

        for i in range(len(matrix)):
            tmp = []
        
            # Creates the column array
            for j in range(len(matrix)):
                tmp.append(matrix[j][i])
                
            for digit in digits:
                if digit not in tmp or digit not in matrix[i]:
                    return False
        
        return True
