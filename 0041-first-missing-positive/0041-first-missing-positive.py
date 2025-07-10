class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        nums = [num for num in nums if num > 0]
        nums = list(set(nums))
        nums.sort()
        val = 1
        for i in range(len(nums)):
            if val != nums[i]:
                return val
            val += 1
        return val



        

            
        