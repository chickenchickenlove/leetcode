
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        mv, result = 1, [0, 0]
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                mv = 2
                result = [i, i+1]


        for diff in range(2, len(s)):
            # 2에 대해서 다 채워보는 거지 ->
            for i in range(len(s)-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1] == True:
                    dp[i][j] = True
                    # if j-i+1 > mv:
                    result = [i,j]


        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         if i > j : continue
        #         if mv < j-i+1 and dp[i][jk]:
        #             mv = j-i+1
        #             result = s[i:j + 1]

        a, b = result
        return s[a:b+1]



for s in ["babad"]:
    print(Solution().longestPalindrome(s))

