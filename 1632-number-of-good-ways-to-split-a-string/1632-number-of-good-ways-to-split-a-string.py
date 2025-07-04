class Solution(object):
    def numSplits(self, s):
         n = len(s)
         left_count = [0]*n
         right_count = [0]*n

         leftSet = set()
         rightSet = set()

         for i in range(len(s)):
            leftSet.add(s[i])
            left_count[i] = len(leftSet)

         for i in range(len(s)-1,-1,-1):
            rightSet.add(s[i])
            right_count[i] = len(rightSet)
         
         count = 0

         for i in range(len(s)-1):
            if left_count[i] == right_count[i+1]:
              count += 1
        
         return count
             
        

