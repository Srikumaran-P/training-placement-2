class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_to_int_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0
        
        while i < len(s):
            if i < len(s) - 1 and roman_to_int_dict.get(s[i]) < roman_to_int_dict.get(s[i + 1]):
                total -= roman_to_int_dict.get(s[i])
            else:
                total += roman_to_int_dict.get(s[i])

            i += 1

        return total
