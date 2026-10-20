class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        # dp array should contain length of subsequence ending @ elem
        # in dp array

        for n in range(len(nums)):
            for i in range(0, n):
                if nums[n] > nums[i]:
                    current = dp[i] + 1
                    dp[n] = max(dp[n], current)
        
        return max(dp)


