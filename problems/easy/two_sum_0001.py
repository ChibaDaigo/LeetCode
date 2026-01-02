from utils import *

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        length = len(nums)
        answer = {}

        for i in range(length):
            compl = target - nums[i]

            if compl in answer:
                return [answer[compl], i]
            else:
                answer[nums[i]] = i

        # length = len(nums)

        # for i in range(length):
        #     for j in range(i+1, length):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #         else:
        #             next
