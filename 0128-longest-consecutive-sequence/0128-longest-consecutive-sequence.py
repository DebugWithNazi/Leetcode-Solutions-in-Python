class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in nums:
                streak = 1
                cur_num = num

                while cur_num+1 in nums:
                    streak += 1
                    cur_num += 1

                longest = max(longest, streak)
        return longest
 
                    
                

        
        



        