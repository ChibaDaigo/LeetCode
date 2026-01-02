from utils import *

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}

        for i, num in enumerate(nums):
            compl = target - num

            if compl in seen:
                return [seen[compl], i]

            seen[num] = i

        # length = len(nums)

        # for i in range(length):
        #     for j in range(i+1, length):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #         else:
        #             next
