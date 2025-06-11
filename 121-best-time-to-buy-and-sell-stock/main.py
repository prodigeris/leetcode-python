from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        window = 1
        top = 0
        while i < len(prices) - 1:
            d = prices[window] - prices[i]
            if top < d:
                top = d
            window += 1
            if window == len(prices):
                i += 1
                window = i+1
        return top
