from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for key, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target - num], key]
            seen[num] = key
