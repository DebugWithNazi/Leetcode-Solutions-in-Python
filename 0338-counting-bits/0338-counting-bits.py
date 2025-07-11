class Solution(object):
    def countBits(self, n):
        ans = []

        for i in range(n+1):
            count = self.oneBits(i)
            ans.append(count)
        
        return ans

    def oneBits(self,n):
        res = 0
        while n > 0:
            res += n % 2
            n = n >> 1
        return res
    






















        # ans = []
        # res = 0
        # for i in range(n+1):
        #     while i:
        #         if i % 2 == 1:
        #             res += 1
        #         i = i >> 1
        #     ans.append(res)
        #     res = 0
        # return ans
                
        