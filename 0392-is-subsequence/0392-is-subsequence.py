class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True
        elif not t:
            return False
        i, j = 0,0

        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1 
            i+= 1
        
        return len(s) == j

        


















        # i,j = 0,0

        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # return i == len(s)

        
        # if not s and t:
        #     return True 
        # elif s and not t:
        #     return False
        # elif not s and not t:
        #     return True

        # sLen = len(s)
        # spointer = 0
        # tpointer = 0
        # count = 0
        # while tpointer < len(t):
        #     if s[spointer] == t[tpointer]:
        #         count += 1
        #         if count == sLen:
        #             return True
        #         spointer += 1
        #     tpointer += 1
       
        # return False


        