class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap ={}
        tMap = {}
        list1 = []
        count = 1
        for char in s:
            if char not in sMap:
                sMap[char] = count 
                count += 1
            list1.append(sMap[char])

        count = 1
        list2 = []
        for char in t:
            if char not in tMap:
                tMap[char] = count 
                count += 1
            list2.append(tMap[char])
        
        for i,j in zip(list1,list2):
            if i != j:
                return False
        
        return True
        




        