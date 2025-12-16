import pytest
from problems.easy.valid_parentheses_0020 import Solution

class TestValidParentheses:
  @pytest.fixture
  def solution(self):
    return Solution()

  @pytest.mark.parametrize("s, expected", [
    ('()', True),
    ('()[]{}', True),
    ('(]', False),
    ('([)]', False),
    ('{[]}', True),
  ])
  def test_valid_parentheses(self, solution, s, expected):
    assert solution.isValid(s) == expected
