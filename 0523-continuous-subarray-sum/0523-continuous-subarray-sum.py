class Solution(object):
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        hashMap = {0:-1}
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]

            remainder = sum % k

            if remainder in hashMap:
                if i - hashMap[remainder] >= 2:
                    return True
            else:
                hashMap[remainder] = i
        
        return False
