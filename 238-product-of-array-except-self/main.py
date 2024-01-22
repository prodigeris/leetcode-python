import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                answers[i] = answers[i + 1] * nums[i + 1]
        pre = 1
        for i in range(len(nums)):
            if i > 0:
                pre *= nums[i - 1]
            answers[i] *= pre

        return answers


print(Solution().productExceptSelf([1,2,3,4]))
