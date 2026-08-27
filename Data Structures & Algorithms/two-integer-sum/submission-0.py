class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i, n in enumerate(nums):
            res = target - n
            if res in cache: return [cache[res], i]
            else: cache[n] = i



        

