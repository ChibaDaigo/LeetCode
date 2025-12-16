class Solution:
    def isValid(self, s):
        stack = []

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ')':
                    if stack.pop() != '(':
                        return False
                if char == '}':
                    if stack.pop() != '{':
                        return False
                if char == ']':
                    if stack.pop() != '[':
                        return False
        if len(stack) != 0:
            return False
        else:
            return True