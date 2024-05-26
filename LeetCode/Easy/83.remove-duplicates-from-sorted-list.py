#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Dummy = ListNode()
        current = Dummy
        elements = set()
        while head:
            if head.val not in elements:
                elements.add(head.val)
                current.next = ListNode(head.val)
                current = current.next
            
            head = head.next
        
        return Dummy.next
        
# @lc code=end

