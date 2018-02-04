class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for start in range(length / 2):
            for i in range(start, length - start - 1):
                tmp = matrix[start][i]
                matrix[start][i] = matrix[length -1 - i][start]
                matrix[length - 1 - i][start] = matrix[length - 1 - start][length - 1 - i]
                matrix[length - 1 - start][length - 1 - i] = matrix[i][length - 1 - start]
                matrix[i][length - 1 - start] = tmp
                
        