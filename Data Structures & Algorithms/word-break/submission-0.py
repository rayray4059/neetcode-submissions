class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = {}

        def solve(i):

            if i == len(s):
                return True
            if i in dp and dp[i]:
                return True
            if i in dp and not dp[i]:
                return False
    
            
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    if solve(i + len(w)):
                        dp[i] = True
                        return True
        
            dp[i] = False
            return False

        return solve(0)
            