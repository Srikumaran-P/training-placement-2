class Solution(object):
    parenthesis = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    def isValid(self, s):
        temp = []

        for char in s:
            if char not in self.parenthesis:
                temp.append(char)
            else:
                if not temp: return False
                pop_element = temp.pop()
                if pop_element != self.parenthesis[char]:
                    return False

        return not temp
