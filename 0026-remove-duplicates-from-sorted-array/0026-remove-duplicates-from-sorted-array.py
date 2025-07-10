class Solution(object):
    def removeDuplicates(self, nums):
        left = 0 
        right = left + 1
        count = 1

        while right < len(nums): 
            if nums[left] != nums[right]:
               left += 1
               nums[left] = nums[right]
               count += 1
            right += 1 
        return count

                
        