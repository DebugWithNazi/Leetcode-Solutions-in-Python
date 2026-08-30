class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        counter = Counter(nums)
        count = 0
        for val, k in counter.items():
            count += k*(k-1) // 2

        return count
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #            count += 1

        # return count

