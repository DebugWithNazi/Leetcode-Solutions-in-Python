class Solution(object):
    def shipWithinDays(self, weights, days):
        minCap = max(weights)
        maxCap = sum(weights)
        
        while minCap < maxCap:
            mid = minCap + (maxCap-minCap)//2
            summ = 0 
            d= 1
            for i in range(len(weights)):

                if summ + weights[i] > mid:
                    summ = weights[i]
                    d += 1
                else:
                   summ += weights[i]
                
            
            if d > days:
                minCap = mid + 1
            else:
                maxCap = mid
        
        return minCap


        