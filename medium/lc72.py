def sol(word1, word2, i1, i2, dp):
    # 종료 조건
    # 가장 작은 부분
    if (i1 == -1): return i2 - i1
    if (i2 == -1): return i1 - i2

    # 만약 이전에 계산한 적이 있다면
    if dp[i1][i2] is not None: return dp[i1][i2]

    t = 0
    if word1[i1] == word2[i2]:
        t = sol(word1, word2, i1 - 1, i2 - 1, dp)
    else:
        # insert
        insert = sol(word1, word2, i1, i2 - 1, dp)
        # delete
        delete = sol(word1, word2, i1 - 1, i2, dp)
        # replace
        replace = sol(word1, word2, i1 - 1, i2 - 1, dp)
        t = min(insert, delete, replace) + 1

    dp[i1][i2] = t
    return t


from collections import deque


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[None for _ in range(len(word2))] for _ in range(len(word1))]
        return sol(word1, word2, len(word1) - 1, len(word2) - 1, dp)