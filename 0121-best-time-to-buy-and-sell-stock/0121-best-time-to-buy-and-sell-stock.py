class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        maxProfit = 0

        for price in prices:
            if buy > price:
                buy = price
            profit = price - buy 
            maxProfit = max(maxProfit,profit)
        return maxProfit


        