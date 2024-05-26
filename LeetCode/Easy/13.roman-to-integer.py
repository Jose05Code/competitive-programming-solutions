#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start

"""
    Time Complexity: O(n)
        Algorithm: Math
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            #normal cases
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000,
            #special cases
            'IV': 4, 'IX': 9, 'XL': 40,
            'XC': 90, 'CD': 400, 'CM': 900
        }
        
        # initialize the result and the index
        result = 0
        i=0
        
        # iterate through the string
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in map: # check for special cases
                result += map[s[i:i+2]]
                i += 2
            else:
                result += map[s[i]] # normal cases
                i+=1
                
        return result
        
# @lc code=end

