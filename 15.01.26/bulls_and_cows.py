class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        freq={

        }
        bull=0
        cow=0
        for i in secret:
            freq[i]=freq.get(i,0)+1
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1
                freq[secret[i]]-=1
                
        for i in range(len(secret)):
            if secret[i] != guess[i]:
                if freq.get(guess[i], 0) > 0: #if the frequency of char is greater than 0
                    cow += 1
                    freq[guess[i]] -= 1
                    
        return "{}A{}B".format(bull,cow)
        
