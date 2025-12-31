class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if(target in matrix[i]):
                return True
        return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
