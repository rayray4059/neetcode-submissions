class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            # we are in the rotated section
            if nums[right] < nums[mid]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            
            # we are not in rotated section
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            
        
        if nums[left] == target:
            return left
        else:
            return -1
