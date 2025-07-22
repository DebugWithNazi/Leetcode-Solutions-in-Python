class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        countS1 = Counter(s1)
        countS2 = Counter(s2[:len_s1])

        
        for i in range(len_s1, len_s2):
            if countS1 == countS2:
                return True
        
            countS2[s2[i]] += 1
            countS2[s2[i-len_s1]] -= 1

            if countS2[s2[i-len_s1]] == 0:
                del countS2[s2[i-len_s1]]
            
        return False






        

        