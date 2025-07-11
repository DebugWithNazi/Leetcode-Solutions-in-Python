class Solution(object):
    def getSum(self, a, b):
        
        mask = 0xffffffff
        while (b & mask) > 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return (a & mask) if b > 0 else a

        






















        # mask = 0xffffffff
        # while (b&mask) > 0:
        #     a,b = a^b, (a & b) << 1
        # return (mask&a) if b > 0 else a
        