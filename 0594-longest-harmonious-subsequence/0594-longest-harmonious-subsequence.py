class Solution:
    def findLHS(self, nums: List[int]) -> int:

        count = Counter(nums)
        long_sub = 0

        for i in range(len(nums)):
            if nums[i] + 1 in count:
                long_sub = max(long_sub, (count[nums[i]] + count[nums[i]+1]))

        return long_sub

        