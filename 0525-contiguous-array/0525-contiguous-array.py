class Solution(object):
    def findMaxLength(self, nums):
        n = len(nums)
        hashMap = {0:-1}
        currSum = 0
        result = 0

        for i in range(len(nums)):
            currSum += 1 if nums[i] == 1 else -1

            if currSum in hashMap:
                result = max(result, i-hashMap[currSum])
            else:
                hashMap[currSum] = i
        return result



        