#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        size = len(nums3)
        if size % 2 == 0:
            return (nums3[size // 2] + nums3[size // 2 - 1]) / 2
        else:
            return nums3[size // 2]
# @lc code=end

