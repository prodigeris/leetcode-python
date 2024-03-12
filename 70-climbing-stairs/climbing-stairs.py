class Solution:

    def __init__(self, ):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        if n in self.cache:
            return self.cache[n]
        r = self.climbStairs(n-2) + self.climbStairs(n-1)
        self.cache[n] = r
        return r


print("sprendimas", Solution().climbStairs(6))