class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        if s[0] == '0':
            return 0

        for i in range(len(s)):

            if s[i] == '1' and (i + 2) <= len(s):
                dp[i + 2] += dp[i]
            elif s[i] == '2' and (i + 2) <= len(s) and int(s[i + 1]) <= 6:
                dp[i + 2] += dp[i]
            
            if s[i] != "0":
                dp[i + 1] += dp[i]

        print(dp)
        return dp[len(s)]



            


