class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n > 0:
            val = n % 2
            if val == 1:
                count += 1
            n = n >> 1
        return count
        


















        # res = 0
        # while n:
        #     res += n % 2
        #     n = n >> 1
        # return res
        # # res = 0
        # # while n:
        #     n = n & (n-1)
        #     n = n >> 1
        # return res

        
            

        