import functools
class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        d = 10**9 + 7
        n = high+1
        dp = [0] * n

        # init
        dp[zero] += 1
        dp[one] += 1

        # zero < one인 경우, zero -> one으로 오는 경우의 수도 더해야 함.
        for i in range(high+1):
            if i-zero > 0:
                dp[i] += dp[i-zero] % d
            if i-one > 0:
                dp[i] += dp[i-one] % d

        def fun(x, y):
            x += y
            return x % d
        return functools.reduce(fun, dp[low:high+1]) % d

