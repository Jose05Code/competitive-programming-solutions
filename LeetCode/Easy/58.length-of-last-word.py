#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Returns the length of the last word in the given string.

        Parameters:
        s (str): The input string.

        Returns:
        int: The length of the last word in the string.
        """
        return len(s.split()[-1])

