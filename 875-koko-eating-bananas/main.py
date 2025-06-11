from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_speed = right
        while left <= right:
            k = (left+right) // 2
            if self.howManyHoursToEat(piles, k) > h:
                left = k+1
            else:
                right = k-1
                min_speed = k

        return min_speed

    def howManyHoursToEat(self, piles: List[int], k: int):
        t = 0
        for pile in piles:
            t += math.ceil(pile/k)
        return t
