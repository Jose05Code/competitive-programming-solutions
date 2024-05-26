#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        fibonacci = [0,1]
        for i in range(2,n+1):
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
            
        return fibonacci[n]
        
# @lc code=end

