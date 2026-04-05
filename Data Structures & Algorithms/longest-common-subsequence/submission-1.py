class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        note that the subsequence could check 3 things:
            - left: text1 without the letter
            - up: text2 without the letter
            - up-left: text1 and text2 without the letter

            Only if up-left is equal could we add 1 to the count, since this ensures
            that the letter is new
        """

        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1] :
                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        

        return dp[n1][n2]


        