class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        m, n = len(text1), len(text2)
        # dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]: # char at positions i,j is equal. adding 1.
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else: # char does not match. taking max of left and down in dp array
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        # for x in dp:
        #     print(x)
        return dp[m][n] # result is at 0th index

s = Solution()
print(s.longestCommonSubsequence('abcde','ace'))