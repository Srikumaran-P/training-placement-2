
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        max_len = 0
        
        def check_palindrome(i, j, s):
            # Expand outwards while characters match
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            # Return the palindrome substring and its length
            # Note: We stepped back one too far, so start is i+1, end is j
            return s[i+1:j], j - (i + 1)

        for l in range(len(s)):
            # Odd length palindromes (center is a character)
            odd, odd_len = check_palindrome(i=l, j=l, s=s)
            # Even length palindromes (center is between characters)
            even, even_len = check_palindrome(i=l, j=l+1, s=s)
            
            if max_len < odd_len:
                max_len = odd_len
                res = odd
            if max_len < even_len:
                max_len = even_len
                res = even
                
        return res
