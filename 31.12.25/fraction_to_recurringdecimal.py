class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        
        result = []
        
        # Handle negative numbers
        if (numerator < 0) != (denominator < 0):
            result.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))
        
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        
        result.append(".")
        remainder_map = {}  # remainder -> index in result
        
        while remainder != 0:
            if remainder in remainder_map:
                idx = remainder_map[remainder]
                result.insert(idx, "(")
                result.append(")")
                break
            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(result)

# Example usage
sol = Solution()
print(sol.fractionToDecimal(1, 2))    # Output: "0.5"
print(sol.fractionToDecimal(2, 1))    # Output: "2"
print(sol.fractionToDecimal(4, 333))  # Output: "0.(012)"
