class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i in freq: freq[i] += 1
            else: freq[i] = 1
        
        freq = dict(sorted(freq.items(), key = lambda x:x[1]))
        return list(freq.keys())[-k:]
            