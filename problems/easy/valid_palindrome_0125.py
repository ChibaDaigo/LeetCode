import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        pattern = '[^a-zA-Z0-9]'

        s = re.sub(pattern, '',  s)
        s = s.upper()

        rev = s[::-1]

        center = len(s)/2

        for i in range(center):
            if s[i] != rev[i]:
                return False

        return True

# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """

#         left, right = 0, len(s)-1

#         while left < right:
#             while left < right and not s[left].isalnum():
#                 left += 1
#             while left < right and not s[right].isalnum():
#                 right -= 1
#             if s[left].lower() != s[right].lower():
#                 return False
#             left += 1
#             right -= 1
#         return True