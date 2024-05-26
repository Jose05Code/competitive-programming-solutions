#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists.

        Args:
            l1 (Optional[ListNode]): The head of the first linked list.
            l2 (Optional[ListNode]): The head of the second linked list.

        Returns:
            Optional[ListNode]: The head of the resulting linked list after adding the two numbers.

        """
        dummy = ListNode()
        current = dummy
        sum = 0
        while l1 or l2:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2: 
                sum += l2.val
                l2 = l2.next
            
            current.next = ListNode(sum % 10)
            sum //= 10
            current = current.next
        
        if sum:
            current.next = ListNode(sum)
            
        return dummy.next
# @lc code=end

