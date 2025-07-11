class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        
        while left < right:
            right = right & (right - 1)
        return right








       
     
    
    # brute force
    #  res = left
    #     for i in range(left+1, right + 1):
    #         res =  res & i
    #     return res


        