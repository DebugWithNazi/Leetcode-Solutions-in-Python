class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backTrack(start,current,total):
            if total == target:
               result.append(current[:])
               return 
            if total > target:
                return 
            
            for i in range(start,len(candidates)):
                current.append(candidates[i])
                backTrack(i,current,total + candidates[i])
                current.pop()
        backTrack(0,[],0)
        return result
            






        
