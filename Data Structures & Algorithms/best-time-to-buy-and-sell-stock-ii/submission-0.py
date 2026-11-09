class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        tot = 0
        for i in range(1, len(prices)):
            prev = prices[i - 1]
            diff = prices[i] - prev
            if diff > 0:
                tot += diff
            
        return tot
