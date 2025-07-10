class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0] # 7
        profit = 0
         
        for i in range(1,len(prices)):
            if buy > prices[i]:
                buy = prices[i] # 1
            profit += prices[i] - buy # 0,4,
            buy = prices[i]
        return profit


