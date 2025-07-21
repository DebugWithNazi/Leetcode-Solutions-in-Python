class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        maxHeap = [[-val,char] for char,val in count.items()]
        heapq.heapify(maxHeap)
        
        prev = None
        res = ""
        while maxHeap:
           
            val,char = heapq.heappop(maxHeap)
            res += char
            val += 1

            if prev:
                heapq.heappush(maxHeap,prev)
            if val != 0:
               prev = [val,char]
            else:
                prev = None
        
        return res if len(res) == len(s) else ""
        