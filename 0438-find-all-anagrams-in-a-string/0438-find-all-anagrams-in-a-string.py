class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        countP = {}
        countS = {}
        res = []
        
        for i in range(len(p)):
            countP[p[i]] = countP.get(p[i],0) + 1
            countS[s[i]] = countS.get(s[i],0) + 1
        
        res = [0] if countP == countS else []
        l = 0
        for i in range(len(p),len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1
            countS[s[l]] -= 1
            
            if countS[s[l]] == 0:
                del countS[s[l]]
            l += 1
            if countS == countP:
                res.append(l)
        return res
