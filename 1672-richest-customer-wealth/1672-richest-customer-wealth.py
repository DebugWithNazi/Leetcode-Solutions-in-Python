class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = 0
        maxCount = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                total += accounts[i][j]
            
            maxCount = max(maxCount, total)
            total = 0
        return maxCount
        