class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        currSum = 0
        hashMap = defaultdict(int)
        hashMap[0] = 1

        for curr in nums:
            currSum += curr 
            diff = currSum - k 
            count += hashMap[diff] 
            hashMap[currSum] += 1 
        return count


        