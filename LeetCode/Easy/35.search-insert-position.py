#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Finds the index where the target should be inserted in the given sorted list.

        Args:
            nums (List[int]): The sorted list of integers.
            target (int): The target integer to be inserted.

        Returns:
            int: The index where the target should be inserted.
        """
        # If the target is already in the list, return the index of the target.
        if target in nums:
            return nums.index(target)
        
        # If the target is not in the list, find the index where the target should be inserted.
        for i in range(len(nums)):
            if nums[i] > target:
                return i
            
        # If the target is greater than all the elements in the list, return the length of the list.
        return len(nums)
# @lc code=end

