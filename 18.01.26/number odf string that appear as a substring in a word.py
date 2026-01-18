class Solution(object):
    def numOfStrings(self, patterns, word):
        answer = 0
        #just check if string 1 is in string 2
        for wor in patterns:
            if wor in word:
                answer+=1

        return answer
