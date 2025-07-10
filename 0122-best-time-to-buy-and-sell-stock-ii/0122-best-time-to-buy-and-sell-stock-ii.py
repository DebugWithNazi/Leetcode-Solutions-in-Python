class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0] # 7
        profit = 0
         
        for i in range(1,len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            profit += prices[i] - buy
            buy = prices[i]
        return profit


