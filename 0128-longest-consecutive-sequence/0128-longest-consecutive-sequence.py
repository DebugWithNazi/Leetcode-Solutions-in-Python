class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSeq = 0

        for num in numSet:
            if num-1 not in numSet:
                streak = 1
                curr = num

                while curr + 1 in numSet:
                     streak += 1
                     curr += 1
                
                maxSeq = max(maxSeq,streak)
        return maxSeq

        


        