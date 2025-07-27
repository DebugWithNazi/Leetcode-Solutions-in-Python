class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashMap = {}
        string = ""
        final = []

        if len(s) < 10:
            return []

        for i in range(10):
            string += s[i]
        
        hashMap[string] = 1

        for i in range(10,len(s)):
            string = string[1:] + s[i] 
            if string not in hashMap:
                hashMap[string] = 1
            else:
                hashMap[string] += 1
        
        for key,value in hashMap.items():
            if value >= 2:
                final.append(key)
        
        return final

        