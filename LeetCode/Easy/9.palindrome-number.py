#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
    
"""
    Time Complexity: O(log10(n))
        Algorithm: Math
"""

"""
    Time Complexity O(n)
    String Conversion
    x==int(str(x)[::-1])
"""
    
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: # if x is negative, it is not a palindrome
            return False
        
        # initialize the reversed number and the original number
        reversed_x = 0
        original_x = x
        
        # reverse the number
        while original_x:
            reversed_x = (reversed_x + original_x % 10)*10
            original_x //= 10
        return reversed_x//10 == x
        
        
# @lc code=end

