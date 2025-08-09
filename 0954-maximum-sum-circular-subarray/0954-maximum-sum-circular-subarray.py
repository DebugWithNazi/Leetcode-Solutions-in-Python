class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Initialize global max/min with the first element
        globMax = nums[0]
        globMin = nums[0]
        
        # Current max/min subarray sums (Kadane's variables)
        currMax, currMin = 0, 0
        
        # Total sum of the array
        total = 0

        # Loop through each number
        for num in nums:
            # Kadane for max subarray
            currMax = max(currMax + num, num)
            globMax = max(globMax, currMax)

            # Kadane for min subarray
            currMin = min(currMin + num, num)
            globMin = min(globMin, currMin)

            # Keep total sum for wrap-around calculation
            total += num

        # If all numbers are negative, return globMax directly
        if globMax <= 0:
            return globMax
        
        # Otherwise, consider wrap-around case
        return max(globMax, total - globMin)



