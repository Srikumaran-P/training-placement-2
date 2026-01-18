class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        x,y,z = "","",""
        for i in firstWord:
            x += (str(ord(i)-ord("a")))
        for i in secondWord:
            y += (str(ord(i)-ord("a")))
        for i in targetWord:
            z += (str(ord(i)-ord("a")))
        return  int(x)+int(y) == int(z)
