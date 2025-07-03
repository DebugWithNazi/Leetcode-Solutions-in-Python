class Solution(object):
    def isPossible(self, nums):
        freq = Counter(nums)
        appendFreq = defaultdict(int)

        for num in nums:
            if freq[num] == 0:
                continue
            
            if appendFreq[num - 1] > 0:
                appendFreq[num - 1] -= 1
                appendFreq[num] += 1
                freq[num] -= 1
            
            elif freq[num+1] > 0 and freq[num+2] >0:
                 freq[num] -=1 
                 freq[num+1] -= 1
                 freq[num+2]-=1
                 appendFreq[num+2] += 1
            
            else:
                return False
        return True