from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_wall, right_wall = 1, 1
        n = len(nums)
        left_array, right_array = [0] * n, [0] * n
        for i in range(n):
            j = n-i-1
            left_array[i] = left_wall
            left_wall *= nums[i]
            right_array[j] = right_wall
            right_wall*=nums[j]

        result = []
        for i in range(n):
            result.append(left_array[i]*right_array[i])
        return result

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    so = Solution()
    print(so.productExceptSelf(nums))
