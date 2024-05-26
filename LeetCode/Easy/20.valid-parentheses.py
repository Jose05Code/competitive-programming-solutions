#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#



""" 
    Problem Description:
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. An empty string is also considered valid.
    Implement a function isValid(s: str) -> bool to solve the problem.
    Time Complexity: O(n)
    Algorithm: Stack
"""


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # If the length of the string is odd, then it is not valid
        if len(s) % 2 != 0:
            return False

        # Map to store the opening and closing brackets
        bracket_map = {"(": ")", "{": "}", "[": "]"}

        # Stack to store the opening brackets
        opening_brackets = []

        # Iterate through the string
        for char in s:
            # If the character is an opening bracket, then push it to the stack
            if char in bracket_map:
                opening_brackets.append(char)
            # If the character is a closing bracket
            else:
                # If there are no opening brackets left or the closing bracket doesn't match the last opening bracket, return False
                if len(opening_brackets) == 0 or char != bracket_map[opening_brackets.pop()]:
                    return False

        # If the stack is not empty, then return False because there are some opening brackets left
        return len(opening_brackets) == 0

# @lc code=end
