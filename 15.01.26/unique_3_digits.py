class Solution:
    def totalNumbers(self, digits):
        unique_numbers = set()
        n = len(digits)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k:  # Ensure all indices are different
                        if digits[i] != 0:  # First digit should not be zero
                            if digits[k] % 2 == 0:  # Last digit should be even
                                number = digits[i] * 100 + digits[j] * 10 + digits[k]
                                unique_numbers.add(number)
        
        return len(unique_numbers)
