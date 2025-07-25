class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        windowSize = 0
        maxFreq = 0
        hashMap = {}

        for right in range(len(s)):
            if s[right] not in hashMap:
                hashMap[s[right]] = 1
            else:
                hashMap[s[right]] += 1
            
            windowSize = max(windowSize, hashMap[s[right]])
            if ( right - left + 1 ) - windowSize > k:
                hashMap[s[left]] -= 1
                if hashMap[s[left]] == 0:
                   del hashMap[s[left]]
                left += 1
            maxFreq = max(maxFreq, right - left + 1)
        return maxFreq


