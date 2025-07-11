class Solution(object):
    def singleNumber(self, nums):
        single = nums[0]

        for i in range(1,len(nums)):
            single = single ^ nums[i]
        return single




















        # single = nums[0]
        # for i in range(1,len(nums)):
        #     single = single ^ nums[i]
        # return single
        # dict_map = defaultdict(int)

        # for num in nums:
        #     if num in dict_map:
        #         del dict_map[num]
        #     else:
        #         dict_map[num] = num
        
        # return list(dict_map.values())[0]
       
        
