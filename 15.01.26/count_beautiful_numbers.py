class Solution(object):
    def beautifulNumbers(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        def count(limit):
            digits = map(lambda ch: ord(ch) - ord('0'), str(limit))
            dp = [collections.defaultdict(int) for _ in xrange(2)]
            dp[1][(1, 0)] = 1  

            for digit in digits:
                next_dp = [collections.defaultdict(int) for _ in xrange(2)]
                for is_tight in xrange(2):
                    for (product, digit_sum), count in dp[is_tight].iteritems():
                        max_digit = digit if is_tight else 9
                        for d in xrange(max_digit + 1):
                            next_tight = is_tight and (d == digit)
                            new_product = product * (1 if digit_sum == 0 == d else d)
                            new_sum = digit_sum + d
                            next_dp[next_tight][(new_product, new_sum)] += count
                dp = next_dp

            result = 0
            for is_tight in xrange(2):
                for (product, digit_sum), count in dp[is_tight].iteritems():
                    if digit_sum and product % digit_sum == 0:
                        result += count
            return result

        return count(r) - count(l - 1)
