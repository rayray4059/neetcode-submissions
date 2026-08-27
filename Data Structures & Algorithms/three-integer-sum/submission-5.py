class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            left = i + 1
            right  = len(nums) - 1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] < target: left += 1
                elif nums[left] + nums[right] > target: right -= 1
                else: 
                    trip = [nums[i], nums[left], nums[right]]
                    if trip not in output: output.append(trip)
                    left += 1
                    right -= 1
            
        return output

            

               

