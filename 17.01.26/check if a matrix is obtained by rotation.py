class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        count = 1
        while count <= 4:
            rows = len(mat)
            for i in range(rows):
                for j in range(i):
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
            for row in mat:
                row.reverse()
            if mat == target:
                return True
            else:
                count+=1
        return False
