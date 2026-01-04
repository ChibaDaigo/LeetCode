# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        merged_list = dummy

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1

                list1 = list1.next
            else:
                dummy.next = list2

                list2 = list2.next
            dummy = dummy.next

        dummy.next = list1 or list2

        return merged_list.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """

#         if list1 is None:
#             return list2
#         if list2 is None:
#             return list1

#         merged_list = None

#         list1_current_node = list1
#         list2_current_node = list2

#         if list1_current_node.val < list2_current_node.val:
#             merged_list = list1_current_node

#             list1_current_node = list1_current_node.next
#         else:
#             merged_list = list2_current_node

#             list2_current_node = list2_current_node.next

#         merged_list_current = merged_list

#         while list1_current_node is not None or list2_current_node is not None:
#             if list1_current_node is None:
#                 merged_list_current.next = list2_current_node
#                 break;
#             if list2_current_node is None:
#                 merged_list_current.next = list1_current_node
#                 break;

#             if list1_current_node.val < list2_current_node.val:
#                 merged_list_current.next = list1_current_node

#                 list1_current_node = list1_current_node.next
#             else:
#                 merged_list_current.next = list2_current_node

#                 list2_current_node = list2_current_node.next

#             merged_list_current = merged_list_current.next
#         return merged_list
