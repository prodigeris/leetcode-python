from typing import List


class Solution:
    def __init__(self):
        self.cache = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.checkCost(0, cost)

    def checkCost(self, i: int, cost: List[int]) -> int:
        if len(cost) <= 1:
            return 0
        if i in self.cache:
            return self.cache[i]

        l = self.checkCost(i+1, cost[1:])
        r = self.checkCost(i+2, cost[2:])
        cost = min(cost[0] + l, cost[1] + r)
        self.cache[i] = cost
        return cost



print(Solution().minCostClimbingStairs([10, 15, 20]))
