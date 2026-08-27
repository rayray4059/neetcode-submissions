class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < prices[buy] and i > buy:
                buy = i

            profit = prices[i] - prices[buy]
            
            if maxProfit < profit:
                maxProfit = profit
        
        if maxProfit > 0: 
            return maxProfit
        else:
            return 0 
        