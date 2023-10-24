from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self._h = nums

    def add(self, val: int) -> int:
        heapq.heappush(self._h, val)
        while len(self._h) > self._k:
            heapq.heappop(self._h)
        return self._h[0]


k = KthLargest(k=2, nums=[])
print(k.add(90))
print(k.add(2))
print(k.add(100))
