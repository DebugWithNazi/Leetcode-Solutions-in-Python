class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backTrack(start,currentList,result):
            if result == target:
                res.append(currentList[:])
                return 
            if result > target: 
                return 

            for i in range(start,len(candidates)):
                currentList.append(candidates[i])
                backTrack(i,currentList, result + candidates[i])
                currentList.pop()
        
        backTrack(0,[],0)
        return res