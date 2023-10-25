from typing import List


# 처음에는 다음과 같이 접근함
# 1. 모든 가능한 팰린드롬을 구함.
# 2. 팰린 드롬의 (1,2) (2,4)를 붙여넣는 식으로 찾았음.
# 그런데 굳이 그렇게 할 필요가 없음. 떨어져있는 게 아니라 붙어있는 것을 해야하기 때문임.

# 앞에서부터 팰린드롬을 DFS를 하면 됨.
# 그런데 여기서 중요한 것은 이어지는 팰린드롬을 해야함.
# 팰린드롬이면 다음 팰린드롬을 찾아서 DFS를 함. 즉, DP + DFS를 조합해야 함.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        # for i in range(n):
        #     dp[i][i] = True
        result = []

        def dfs(string, start, acc):
            # 종료 조건은?
            if start == len(string):
                result.append([k for k in acc])
            for end in range(start, len(string)):
                if s[start] == s[end] and (end-start <= 2 or dp[start+1][end-1]):
                    dp[start][end] = True
                    acc.append(s[start:end + 1])
                    dfs(string, end + 1, acc)
                    acc.pop()

        dfs(s, 0, [])
        return result

# Solution().partition("aab")


class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]

        for diff in range(2, n):
            for i in range(diff, n):
                j = i - diff
                dp[j][i] = (dp[j + 1][i - 1] and s[j] == s[i])

        d = [[0 for _ in range(n)] for _ in range(n)]

        for j in range(n):
            if dp[0][j]:
                d[0][j] = 1

        rrrrr = 9876543210
        for i in range(1, n):
            for j in range(n):
                if dp[i-1][j-1] and dp[i][j]:
                    d[i][j] = d[i-1][j-1] + 1
                    if j == n-1 and d[i][j] > 0:
                        rrrrr = min(rrrrr, d[i][j])
        print(rrrrr)
        return rrrrr

        # for i in range(n):
        #     for j in range(n):



Solution().minCut("aab")



Solution().minCut('ababababababababababababcbabababababababababababa')