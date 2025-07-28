class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        if len(s) < k:
            return 0
            
        hashMap = Counter(s)

        for char in hashMap:
            if hashMap[char] < k:
                parts = s.split(char)
                maxLen = 0
                for part in parts:
                    result = self.longestSubstring(part,k)
                    maxLen = max(maxLen, result)
                return maxLen
        
        return len(s)

            

        