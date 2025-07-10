class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        majority = n//2

        hashMap = defaultdict(int)

        for num in nums:
            hashMap[num] += 1
        
        for num in nums:
            if hashMap[num] >majority:
                return num 
























        # limit = len(nums)//2

        # myDict = {}

        # for i in range(len(nums)):
        #     if nums[i] not in myDict:
        #         myDict[nums[i]] = 1
        #     else:
        #         myDict[nums[i]] += 1
            
        # for key in myDict:
        #     if myDict[key] > limit:
        #         return key
        
         