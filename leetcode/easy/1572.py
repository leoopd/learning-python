# 1572. Matrix Diagonal Sum

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i = 0
        j = len(mat[0])-1
        diag_sum = 0
        for element in mat:
            if i == j:
                diag_sum += element[i]
            else:
                diag_sum += element[i] + element[j]
            i += 1
            j -= 1
        return diag_sum
