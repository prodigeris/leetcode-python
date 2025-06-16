from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i: int, path: List[int]) -> None:
            if i == len(nums):
                res.append(path)
                return
            backtrack(i + 1, path)
            backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return res
