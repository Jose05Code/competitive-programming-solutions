#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Adds one to the given list of digits.

        Args:
            digits (List[int]): The list of digits.

        Returns:
            List[int]: The updated list of digits after adding one.
        """
        # Iterate through the list of digits in reverse order.
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                # If the digit is not 9, add one to it and return the updated list.
                digits[i] += 1
                return digits

        # If the loop completes, it means all digits were 9.
        return [1] + digits
        
# @lc code=end

