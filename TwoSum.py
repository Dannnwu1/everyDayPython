from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            d[num] = i

        for i, num in enumerate(nums):
            completion = target - num
            if completion in d and d[completion] != i:
                return [i, d[completion]]

        return [-1, -1]
