class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        seen = set()
        curr_window = 0
        result = 0

        for j in range(len(nums)):

            while nums[j] in seen:
                curr_window -= nums[i]
                seen.remove(nums[i])
                i += 1

            curr_window += nums[j]
            seen.add(nums[j])
            if j - i + 1 == k:
                result = max(result,curr_window)
                curr_window -= nums[i]
                seen.remove(nums[i])
                i += 1

        return result     
        