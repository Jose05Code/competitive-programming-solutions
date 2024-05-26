#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    """
    Returns the index of the first occurrence of 'needle' in 'haystack', or -1 if 'needle' is not part of 'haystack'.

    Algorithm:
        This function uses Python's built-in 'in' operator to check if 'needle' is in 'haystack'. If it is, the function
        uses the 'index()' method to find the index of the first occurrence of 'needle'. If 'needle' is not in 'haystack',
        the function returns -1.

    Time Complexity:
        The time complexity is O(n*m), where n is the length of 'haystack' and m is the length of 'needle'. This is because
        in the worst case scenario, the 'in' operator and the 'index()' method each need to scan through the entire 'haystack'
        for each character in 'needle'.

    Parameters
    ----------
    haystack : str
        The string in which to search for 'needle'.

    needle : str
        The string to search for in 'haystack'.

    Returns
    -------
    int
        The index of the first occurrence of 'needle' in 'haystack', or -1 if 'needle' is not part of 'haystack'.
    """
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle in haystack:
            return haystack.index(needle)
        
        else:
            return -1
        
        
# @lc code=end

