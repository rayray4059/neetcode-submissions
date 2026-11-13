class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                left, right = b + 1, len(nums) - 1

                while left < right:
                    current = nums[left] + nums[right] + nums[b] + nums[a]
                    
                    if current < target:
                        left += 1
                    if current == target:
                        quad = sorted([nums[left], nums[right], nums[a], nums[b]])
                        if quad not in out:
                            out.append(quad)
                        left += 1
                        right -= 1
                    
                    if current > target:
                        right -= 1
        
        return list(out)



