class Solution:
    def jump(self, nums: List[int]) -> int:

        farthest = 0
        counter,jump = 0,0
        for i in range(len(nums)-1):
            farthest = max(farthest,i + nums[i])

            if i == counter:
                jump += 1
                counter = farthest
        return jump

        