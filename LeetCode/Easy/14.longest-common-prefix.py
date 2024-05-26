#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    """
    Returns the longest common prefix string amongst an array of strings.
    A prefix of a string is a substring that starts from the beginning.

    Parameters
    ----------
    strs : List[str]
        A list of strings.

    Returns
    -------
    str
        The longest common prefix of the strings in the input list. If there is no common prefix, returns an empty string.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        prefix = ""
        for i in range(len(strs[0])):
            if all(word[i] == strs[0][i] for word in strs):
                prefix += strs[0][i]
            else:
                break
            
        return prefix
            
                
                
# @lc code=end

