class Solution(object):
    def longestCommonPrefix(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[int]
        """
        n = len(words)

        if k == n:
            return [0] * n

        indices = sorted(range(n), key=lambda i: words[i])

        def getPrefixLength(a, b):
            length = min(len(a), len(b))
            i = 0
            while i < length and a[i] == b[i]:
                i += 1
            return i

        longest = -1
        longestWindowStart = -1
        secondLongest = -1

        for i in range(n - k + 1):
            firstWord = words[indices[i]]
            lastWord = words[indices[i + k - 1]]
            prefixLength = getPrefixLength(firstWord, lastWord)

            if prefixLength >= longest:
                secondLongest = longest
                longest = prefixLength
                longestWindowStart = i
            elif prefixLength > secondLongest:
                secondLongest = prefixLength

        answer = [longest] * n

        for i in range(k):
            answer[indices[longestWindowStart + i]] = secondLongest

        return answer
