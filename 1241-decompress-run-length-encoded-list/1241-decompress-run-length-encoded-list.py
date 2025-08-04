class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            val = nums[i+1]
            final.extend([val] * freq)
        return final

        