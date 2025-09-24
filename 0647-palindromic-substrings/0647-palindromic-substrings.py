class Solution(object):
    def countSubstrings(self, s):
       # ---- Optimized Approach ----
       count = 0 
       for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                 count += 1 
                 l -= 1
                 r += 1
            
            l = i 
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                  count += 1
                  l -= 1
                  r += 1
       return count
        

        # ---- Brute Force Approach ----

        # count = 0
        # def palindrom(i, j):
        #     while i <= j:
        #         if s[i] == s[j]:
        #             i += 1
        #             j -= 1
        #         else:
        #           return False
        #     return True
                

        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         val = palindrom(i,j)
        #         if val:
        #             count += 1
        # return count