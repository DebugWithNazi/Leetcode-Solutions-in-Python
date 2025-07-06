class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        maxHeight = 0

        while l < r:
            area = (r - l) * min(height[l],height[r])
            maxHeight = max(area, maxHeight)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxHeight 



        #Brute Force
        # maxHeight = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = (j-i) * min(height[i],height[j])
        #         maxHeight = max(area, maxHeight)

        # return maxHeight
