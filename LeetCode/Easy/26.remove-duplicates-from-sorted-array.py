#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from the list nums and returns the length of the list after removal.

        Algorithm:
            This function uses a set to eliminate duplicates from the list. It then sorts the set (which converts it to a list)
            and updates the original list with the sorted, unique values.

        Time Complexity:
            The time complexity is O(n log n), where n is the length of the list. This is because converting a list to a set is O(n),
            sorting is O(n log n), and updating the list is O(n). The dominant term is O(n log n).

        Parameters
        ----------
        nums : List[int]
            A sorted list of integers from which duplicates are to be removed.

        Returns
        -------
        int
            The length of the list after removing duplicates.
        """
        
        # Convert the list to a set to eliminate duplicates
        unique_nums = set(nums)
        
        # Note: when sorting a set, it is converted to a list
        # so we can use the [:] notation to update the original list
        nums[:] = sorted(unique_nums)
        
        # Return the length of the list
        return len(nums)


# @lc code=end
