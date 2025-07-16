class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = {}
        goodPair = 0
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1 

        for k,v in hashMap.items():
            goodPair += (v*(v-1)//2)  

        return goodPair              
        