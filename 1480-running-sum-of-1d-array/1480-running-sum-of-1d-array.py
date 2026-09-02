class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        totalSum = 0
        for num in nums:
            totalSum += num
            result.append(totalSum)
        
        return result
            
        