class Solution(object):
    def threeSum(self, nums):
        final = set()
        nums.sort()
        for i in range(len(nums)):
            first = nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                    total = first+nums[left]+nums[right] 
                    if total == 0:
                        final.add((first,nums[left],nums[right]))
                        left += 1
                        right -= 1
                    elif total > 0:
                       right -= 1
                    else:
                       left += 1
        return [list(val) for val in final]
                



        

        