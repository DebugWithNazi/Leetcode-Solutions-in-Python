class NumArray(object):
    
    def __init__(self, nums):
        self.prefixArray = [0]*len(nums)
        self.prefixArray[0] = nums[0] # -2
        for i in range(1,len(nums)):
            self.prefixArray[i] = self.prefixArray[i-1] + nums[i]
            # -2,-2,1,-4,-2,-3
        

    def sumRange(self, left, right):
        if left == 0:
            return self.prefixArray[right]
        else:
            return self.prefixArray[right]-self.prefixArray[left-1]

        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)