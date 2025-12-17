# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        prev = None

        while current is not None:
            # memorize next node for loop
            nextnode = current.next

            # relink next node and reload prev
            current.next = prev
            prev = current

            current = nextnode
        return prev
# pytest is not working for this problem because the ListNode class is not defined in the test file.
