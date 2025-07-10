class Solution(object):
    def zeroFilledSubarray(self, nums):
        count = 0
        subArrays = 0
        for num in nums:
            if num == 0:
                count += 1
                subArrays += count
            else:
                count = 0
        return subArrays
            

        