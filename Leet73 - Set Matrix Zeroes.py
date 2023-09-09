class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        first_row = False
        first_col = False
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col = True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if first_row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0