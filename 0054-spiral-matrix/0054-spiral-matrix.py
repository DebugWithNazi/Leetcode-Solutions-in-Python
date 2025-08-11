class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rowBegin = 0
        rowEnd = len(matrix)-1
        colBegin = 0
        colEnd = len(matrix[0])-1
        result = []
        while rowBegin <= rowEnd and colBegin <= colEnd:

            for j in range(colBegin,colEnd+1):
                result.append(matrix[rowBegin][j])

            rowBegin += 1

            for j in range(rowBegin,rowEnd+1):
                result.append(matrix[j][colEnd])

            colEnd -= 1
            
            if rowBegin <= rowEnd:
                for j in range(colEnd,colBegin-1,-1):
                    result.append(matrix[rowEnd][j])

            rowEnd -= 1

            if colBegin <= colEnd:
                for j in range(rowEnd,rowBegin-1,-1):
                    result.append(matrix[j][colBegin])

            colBegin += 1
        
        return result




        