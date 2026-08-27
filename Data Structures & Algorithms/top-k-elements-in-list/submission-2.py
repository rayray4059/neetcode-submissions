class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            if num in count: count[num] += 1
            else: count[num] = 1
        
        for num,freq in count.items():
            output[freq].append(num)
        
        for i in range(len(output))[::-1]:
            for j in output[i]:
                res.append(j)
            if len(res) == k: break
        
        return res

            


            