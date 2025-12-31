class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)  # rows
        m = len(word2)  # cols
        
        D = [[0]*(m+1) for _ in range(n+1)]

        # init first row and col
        for i in range(n+1):
            D[i][0] = i
        for j in range(m+1):
            D[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                cost = 0 if word1[i-1] == word2[j-1] else 1
                delete = D[i-1][j]+1
                insert = D[i][j-1]+1
                replace = D[i-1][j-1] + cost
                D[i][j] = min(delete,insert,replace)

                 
        return D[n][m]        
