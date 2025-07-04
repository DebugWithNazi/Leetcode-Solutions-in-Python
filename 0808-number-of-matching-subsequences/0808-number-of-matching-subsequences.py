class Solution(object):
    def numMatchingSubseq(self, s, words):
        hashMap = defaultdict(list)
        count = 0

        for word in words:
            it = iter(word)
            firstChar = next(it,None)
            hashMap[firstChar].append(it)
        
        for char in s:
            iterator = hashMap[char]
            hashMap[char] = []

            for it in iterator:
                next_char = next(it,None)
                if next_char:
                    hashMap[next_char].append(it)
                else:
                    count += 1
        return count




        

                    
                
                    


        