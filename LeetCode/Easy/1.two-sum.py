#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Returns the indices of two numbers in the list 'nums' such that they add up to 'target'.

        Algorithm:
            This function uses a hash table to store the indices of the elements in 'nums'. It then iterates through 'nums'
            and checks if the complement of each element (i.e., 'target' minus the element) is in the hash table. If the complement
            is found and its index is different from the index of the current element, the function returns these two indices.

        Time Complexity:
            The time complexity is O(n), where n is the length of the list 'nums'. This is because the function iterates twice
            through 'nums', but the iterations are not nested, so the complexity is linear.

        Parameters
        ----------
        nums : List[int]
            A list of integers.

        target : int
            The target integer.

        Returns
        -------
        List[int]
            A list of two indices such that the corresponding numbers in 'nums' add up to 'target'.
        """

        # create a hashtable to store the index of the elements
        hashtable = {}
        # iterate through the list and store the index of the elements
        for i in range(len(nums)):
            hashtable[nums[i]] = i
        # iterate through the list and check if the complement of the element is in the hashtable
        for i in range(len(nums)):
            complement = target - nums[i]  # calculate the complement
            # check if the complement is in the hashtable and the index of the complement is not the same as the index of the element
            if complement in hashtable and hashtable[complement] != i:
                return [
                    i,
                    hashtable[complement],
                ]  # return the index of the element and the index of the complement


# @lc code=end
