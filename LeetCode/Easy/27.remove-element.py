#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


# @lc code=start
class Solution:
    """
    Removes all instances of 'val' from the list 'nums' and returns the length of the list after removal.

    Algorithm:
        This function uses a while loop to continuously remove instances of 'val' from 'nums' as long as 'val' is in 'nums'.
        It uses the list method 'remove()', which removes the first instance of the specified value.

    Time Complexity:
        The time complexity is O(n^2), where n is the length of the list 'nums'. This is because the 'remove()' method is O(n),
        and it is called up to n times in the worst case scenario (when all elements in the list are equal to 'val').

    Parameters
    ----------
    nums : List[int]
        A list of integers.

    val : int
        The integer to be removed from 'nums'.

    Returns
    -------
    int
        The length of the list after removing all instances of 'val'.
    """

    def removeElement(self, nums: List[int], val: int) -> int:

        while val in nums:
            nums.remove(val)

        return len(nums)


# @lc code=end
