class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] - 1 in seen: continue
            curr = nums[i]
            streak = 1
            while curr + 1 in seen:
                curr += 1
                streak += 1
            res = max(streak, res)
            rem = len(nums) - res
            if res > rem: break
        
        return res


