class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backTrack(remaining):
            if len(remaining) == 0:
                res.append(path[:])
                return 
            
            for i in range(len(remaining)):
                path.append(remaining[i])
                backTrack(remaining[:i] + remaining[i+1:])
                path.pop()
                
        backTrack(nums)
        return res
                
                




        