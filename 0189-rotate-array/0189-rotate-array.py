class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        left = 0
        right = n-1

        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
        
        left = 0
        right = k-1
        while left < right: 
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
            
        left = k
        right = n-1
        while left < right: 
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
        
        return nums

    

        



        # TLE cause of two loops
        # n = len(nums)-1

        # while k != 0:
        #     temp = nums[n]

        #     for i in range(len(nums)-1,0,-1):
        #         nums[i] = nums[i-1]
            
        #     nums[0] = temp
        #     k -= 1
        # return nums

            




        