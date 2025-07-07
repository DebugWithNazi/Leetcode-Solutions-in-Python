class Solution(object):
    def subarraysDivByK(self, nums, k):
        count = 0 
        currSum = 0
        hashMap =defaultdict(int)
        hashMap[0] = 1

        for num in nums:
            currSum += num
            diff = currSum % k
            count += hashMap[diff]
            hashMap[diff] += 1
        return count
           
           



            


        