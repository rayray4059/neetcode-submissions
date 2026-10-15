class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        house1 = nums[0]
        house2 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            current = max(nums[i] + house1, house2)
            house1 = house2
            house2 = current
        
        return house2
            
            
            

      

