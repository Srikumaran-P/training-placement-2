class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        text = list(text.split(' '))
        c = len(text)
        for i in text :
            for j in brokenLetters:
                if j in i:
                    c-=1
                    break
                else : pass
        return c

        
