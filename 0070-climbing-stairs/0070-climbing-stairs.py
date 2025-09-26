class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        elif n == 0:
            return 1
        if n in self.memo:
                return self.memo[n]
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = result
        return result
         