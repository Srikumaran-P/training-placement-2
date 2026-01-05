class Solution(object):
    def generateParenthesis(self, n):
        results = []
        self._generate(n, n, "", results)
        return results

    def _generate(self, open_remaining, close_remaining, current, results):
        if open_remaining == 0 and close_remaining == 0:
            results.append(current)
            return

        if open_remaining > 0:
            self._generate(open_remaining - 1, close_remaining, current + "(", results)

        if close_remaining > open_remaining:
            self._generate(open_remaining, close_remaining - 1, current + ")", results)
