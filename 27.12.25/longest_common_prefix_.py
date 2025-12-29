class Solution(object):
    def longestCommonPrefix(self, strs):
        common_prefix = ''
        longest_str = str(max(strs, key=len))
        iteration = 0
        is_valid_char = True
        stop_iterations = False

        for char in longest_str:
            for string in strs:
                if len(string) < iteration + 1:
                    stop_iterations = True
                    break
                is_valid_char &= char == string[iteration]
            if stop_iterations or not is_valid_char:
                break
            common_prefix += char
            iteration += 1

        return common_prefix
