class Solution(object):
    def reorganizeString(self, s):
        count = Counter(s)
        maxAllowed = (len(s)+1)//2
        if any(freq > maxAllowed for freq in count.values()):
            return ""

        heap = [(-freq,char) for char,freq in count.items()]
        heapq.heapify(heap)
        
        res = ""
        prevFreq, prevChar = 0,0

        while heap:
            freq,char = heapq.heappop(heap)
            res += char

            if prevFreq < 0:
                heapq.heappush(heap,(prevFreq, prevChar))
            
            prevFreq, prevChar = freq+1, char
        return res


           

        


            
         