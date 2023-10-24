import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-num for num in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a == b:
                continue
            heapq.heappush(stones, -abs(a - b))
        return -stones[0] if stones else 0


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
