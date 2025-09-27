class Solution:
    def kthCharacter(self, k: int) -> str:
        initialStr = "a"

        while len(initialStr) < k:
            # strList
            for i in range(len(initialStr)):
                initialStr += chr(ord(initialStr[i]) + 1)
        
        return initialStr[k-1]