class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        
        def backtrack(index, path):

            if sum(path) == target:
                    out.append(path[:])
                    return

            if index == len(nums): 
                return None
            
            # choice 1 include number
            if nums[index] + sum(path) <= target:
                path.append(nums[index])
                backtrack(index, path)
                path.pop()

            # choice 2 skip number
            backtrack(index + 1, path)
        
            return None
        
        backtrack(0, [])
        return out