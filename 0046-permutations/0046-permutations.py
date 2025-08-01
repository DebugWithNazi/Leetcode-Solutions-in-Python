class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTrack(cur_ind):
            if cur_ind == len(nums):
                res.append(nums[:])
                return 
            
            for i in range(cur_ind,len(nums)):
                nums[cur_ind], nums[i] = nums[i],nums[cur_ind]
                backTrack(cur_ind+1)
                nums[cur_ind], nums[i] = nums[i],nums[cur_ind]
        backTrack(0)
        return res
                
                




        