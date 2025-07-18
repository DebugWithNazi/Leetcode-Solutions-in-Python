class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mCount = Counter(magazine)
        
        for char in ransomNote:
            if char in mCount:
               mCount[char] -= 1
               if mCount[char] == 0:
                  del mCount[char]
            else:
                return False
        return True
                  