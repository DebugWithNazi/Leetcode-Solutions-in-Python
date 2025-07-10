class Solution(object):
    def isPalindrome(self, s):
        t = ""
        for i in range(len(s)):
            if s[i].isalnum():
               t += s[i].lower()
        
        left = 0
        right = len(t)-1

        while left < right:
            if t[left] != t[right]:
                return False
            left += 1
            right -= 1
        return True
        



      
        



        