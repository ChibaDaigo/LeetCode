from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(arr: List[int]) -> Optional["ListNode"]:
        if not arr:
            return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def to_list(self) -> List[int]:
        result = []
        curr = self
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: List[Optional[int]]) -> Optional["TreeNode"]:
        """LeetCode形式の配列からTreeNodeを構築"""
        if not arr or arr[0] is None:
            return None

        root = TreeNode(arr[0])
        queue = [root]
        i = 1

        while queue and i < len(arr):
            node = queue.pop(0)

            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1

        return root
