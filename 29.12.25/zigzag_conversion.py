class Solution(object):
    def convert(self, s, numRows):
        # 1. Edge Case: If single row or string is too short, return as is.
        if numRows == 1 or numRows >= len(s):
            return s
        
        result = [] 
        # The full cycle length of the zigzag pattern
        skip_total = (numRows * 2) - 2 
        
        for i in range(numRows):
            # Start index for the current row
            idx = i
            if idx >= len(s): break 
            
            result.append(s[idx])
            
            # Calculate the initial step size
            # For the last row, it's a full cycle. For others: total - 2*i
            skip_iter = skip_total - 2*i if i != numRows - 1 else skip_total
            
            # Special case for the 0th row (always full cycle)
            if i == 0: skip_iter = skip_total
            
            while True:
                idx += skip_iter
                if idx >= len(s):
                    break
                
                result.append(s[idx])
                
                # --- CORE LOGIC: TOGGLE STEP SIZE ---
                # For internal rows, the step size alternates.
                # We flip it by subtracting the current step from the total cycle.
                if i != 0 and i != numRows - 1:
                    skip_iter = skip_total - skip_iter
                    
        return "".join(result)
