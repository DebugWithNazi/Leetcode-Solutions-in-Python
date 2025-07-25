class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            left =  0 
            hashMap = {}
            maxVal = 0
            for right in range(len(s)):
                char = s[right]
                while char in hashMap:
                    del hashMap[s[left]]
                    left += 1
                hashMap[char] = 1
                maxVal = max(maxVal,len(hashMap))
            return maxVal


        
        
        