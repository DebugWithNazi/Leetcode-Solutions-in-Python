class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        final = []
        def patternMatching(value):
            count = 1
            string = []
            patDict = {}

            for char in value:
                if char not in patDict:
                    patDict[char] = count
                    count += 1
                string.append(patDict[char])
            return string
        
        matching = patternMatching(pattern)
        for word in words:
            if matching == patternMatching(word):
               final.append(word)
       
        return final 
                
         




        
        