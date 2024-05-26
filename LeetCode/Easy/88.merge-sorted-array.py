#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2
            return
        
        elements = []
        max_len = max(m,n)
        
        for i in range(max_len):
            if i < m:
                elements.append(nums1[i])
            if i < n:
                elements.append(nums2[i])
            
        nums1[:] = sorted(elements)
        
# @lc code=end

