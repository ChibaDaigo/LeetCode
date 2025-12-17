import pytest
from problems.easy.reversed_linked_list_0206 import Solution

class TestReverseLinkedList:
  @pytest.fixture
  def solution(self):
    return Solution()

  @pytest.mark.parametrize("s, expected", [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([], []),
  ])
  def test_reverse_linked_list(self, solution, s, expected):
    assert solution.reverseList(s) == expected
