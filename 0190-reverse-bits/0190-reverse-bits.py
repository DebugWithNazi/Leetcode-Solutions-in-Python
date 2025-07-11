class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            val = n & 1
            val = val << (31-i)
            res = res | val
            n = n >> 1
        return res























        # result = 0
        # for i in range(32):
        #     lsb = n & 1
        #     reverseLsb = lsb << (31 - i)
        #     result = result | reverseLsb
        #     n = n >> 1
        # return result
        