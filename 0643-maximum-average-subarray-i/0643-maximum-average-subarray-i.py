class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
                # Step 1: Initial window sum
            current_sum = sum(nums[:k])
            max_sum = current_sum

            # Step 2: Slide the window
            for i in range(k, len(nums)):
                current_sum += nums[i] - nums[i - k]
                max_sum = max(max_sum, current_sum)

            # Step 3: Return average
            return max_sum / k
                
        