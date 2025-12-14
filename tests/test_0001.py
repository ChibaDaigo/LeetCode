import pytest
from problems.easy.two_sum_0001 import Solution

class TestTwoSum:
  @pytest.fixture
  def solution(self):
    return Solution()

  @pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
  ])
  def test_two_sum(self, solution, nums, target, expected):
    assert solution.twoSum(nums, target) == expected
