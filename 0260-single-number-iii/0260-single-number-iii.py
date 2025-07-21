class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = nums[0]

        for i in range(1,len(nums)):
            xor = xor ^ nums[i]

        diff = xor & -xor

        group1 = 0
        group2 = 0

        for num in nums:
            if num & diff:
                group1 = group1 ^ num
            else:
                group2 = group2 ^ num
        
        return [group1,group2]

        
                
