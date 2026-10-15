class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        
        def rob_helper(nums, start, end):
            nums = nums[start:end]

            if len(nums) == 1:
                return nums[0]

            if len(nums) == 2:
                return max(nums[0], nums[1])
            
            house1 = nums[0]
            house2 = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                current = max(house1 + nums[i], house2)
                house1 = house2
                house2 = current
            
            return house2

        start = rob_helper(nums, 0, len(nums) - 1)
        end = rob_helper(nums, 1, len(nums))
        
        return max(start, end)