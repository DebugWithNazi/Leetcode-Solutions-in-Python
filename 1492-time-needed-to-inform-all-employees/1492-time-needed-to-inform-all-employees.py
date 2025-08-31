class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        tree = defaultdict(list)

        for emp, mana in enumerate(manager):
            if mana != -1:
                tree[mana].append(emp)
        
        def dfs(emp):
            if not tree[emp]:
                return 0
            maxTime = 0
            for sub in tree[emp]:
                maxTime = max(maxTime, dfs(sub))
            return informTime[emp] + maxTime
        
        return dfs(headID)

        