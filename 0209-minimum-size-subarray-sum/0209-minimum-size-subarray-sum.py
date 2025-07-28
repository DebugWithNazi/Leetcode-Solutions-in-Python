class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0 
        minlen = float('inf')
        totalSum = 0

        for right in range(len(nums)):
            totalSum += nums[right]
            
            while totalSum >= target:
                minlen = min(minlen, right-left + 1) 
                totalSum -= nums[left]
                left += 1
        return minlen if minlen != float('inf') else 0

