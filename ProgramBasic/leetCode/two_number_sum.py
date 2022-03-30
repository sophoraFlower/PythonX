from typing import List
import time


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_length = len(nums)
        for i in range(nums_length - 1):
            for j in range(i + 1, nums_length):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        temp, nums_length = {}, len(nums)
        for item in range(nums_length):
            if nums[item] not in temp:
                temp[target-nums[item]] = item
            else:
                return [temp[nums[item]], item]

    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]


test = Solution()
time_start_01 = time.time()
print(test.twoSum([], 2))
print(test.twoSum([2], 2))
print(test.twoSum([2, 2], 4))
print(test.twoSum([3, 2, 4], 6))
print(test.twoSum([2, 5, 5, 11], 10))
print(test.twoSum([5, 2, 5, 11], 10))
print(test.twoSum([8, 5, 5, 5], 10))
print(test.twoSum([-1, -2, -3, -4, -5], -8))
time_end_01 = time.time()
print(time_end_01-time_start_01)

time_start_02 = time.time()
print(test.twoSum_2([], 2))
print(test.twoSum_2([2], 2))
print(test.twoSum_2([2, 2], 4))
print(test.twoSum_2([3, 2, 4], 6))
print(test.twoSum_2([2, 5, 5, 11], 10))
print(test.twoSum_2([5, 2, 5, 11], 10))
print(test.twoSum_2([8, 5, 5, 5], 10))
print(test.twoSum_2([-1, -2, -3, -4, -5], -8))
time_end_02 = time.time()
print(time_end_02-time_start_02)

time_start_03 = time.time()
print(test.twoSum_3([], 2))
print(test.twoSum_3([2], 2))
print(test.twoSum_3([2, 2], 4))
print(test.twoSum_3([3, 2, 4], 6))
print(test.twoSum_3([2, 5, 5, 11], 10))
print(test.twoSum_3([5, 2, 5, 11], 10))
print(test.twoSum_3([8, 5, 5, 5], 10))
print(test.twoSum_3([-1, -2, -3, -4, -5], -8))
time_end_03 = time.time()
print(time_end_03-time_start_03)
