class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
           
        currSub = sum(nums[:k])
        maxSum = currSub

        for i in range(k,len(nums)):
            currSub += nums[i] - nums[i-k]
            maxSum = max(maxSum, currSub)
        
        return maxSum/k
