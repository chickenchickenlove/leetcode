from typing import List

# OOOO
# OOOX
# OOXO
# OOXX
# ...
# 이런 식으로 재귀적으로 되는데 작은 문제를 이용해서 큰 문제를 풀 수 있음.
# 이 때, recur(now)는 이 부분이 포함되었을 때 하위에서 가장 긴 길이가 얼마인지를 반환하는 값임.
# recur(now) = 1 + (recur(now+1), recur(now+2)...) 중 max가 될 수 있음.


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        N = len(pairs)
        pairs.sort()
        memo = {}
        def recursive(now):
            nonlocal N

            if now in memo:
                return memo[now]
            memo[now] = 1
            for next in range(now+1, N):
                if pairs[now][1] < pairs[next][0]:
                    r = recursive(next)
                    memo[now] = max(memo[now], 1 + r)

            return memo[now]

        ans = 0
        for i in range(N):
            ans = max(ans,recursive(i))

        print(ans)
        return ans


Solution().findLongestChain()