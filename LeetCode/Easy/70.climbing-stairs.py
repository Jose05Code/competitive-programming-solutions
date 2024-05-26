#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb to the top of a staircase with `n` steps.

        Args:
            n (int): The total number of steps in the staircase.

        Returns:
            int: The number of distinct ways to climb to the top.
        """
        fib = [1, 2]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])

        return fib[n - 1]


# @lc code=end
