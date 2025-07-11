class Solution(object):
    def trap(self, height):
        n = len(height)

        left =[0] * n
        right=[0] * n
        count = 0

        left[0] = height[0]
        for i in range(1,len(height)):
            left[i] = max(left[i-1],height[i])
        
        right[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1],height[i])
        

        for i in range(n):
            count += min(left[i],right[i]) - height[i]
        return count



        
        