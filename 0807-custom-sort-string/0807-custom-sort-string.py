class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashMap = Counter(s)
        final = ""
        for char in order:
            if char in hashMap:
                while hashMap[char] != 0:
                    final += char
                    hashMap[char] -= 1
                del hashMap[char]
                          
        
        for char in s:  
            if char in hashMap:
                while hashMap[char] != 0:
                    final += char
                    hashMap[char] -= 1
                del hashMap[char]
        return final
        
        



        