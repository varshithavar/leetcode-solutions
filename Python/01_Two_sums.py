class Solution:
    def twoSum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in lookup:
                return [lookup[diff], i]

            lookup[num] = i


nums = [2, 7, 11, 15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))