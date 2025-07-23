class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        patDict = {}
        count = 1
        string = []
        final = []
        for char in pattern:
            if char not in patDict:
                patDict[char] = count
                string.append(count)
                count += 1
            else:
                string.append(patDict[char])
        
        for word in words:
            newString = []
            count = 1
            patDict = {}
            for char in word:
                if char not in patDict:
                    patDict[char] = count
                    newString.append(count)
                    count += 1
                else:
                    newString.append(patDict[char])
            if string == newString:
                final.append(word)
        return final 
                
         




        
        