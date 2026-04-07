# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next

        current = head
        length = len(stack)

        for _ in range(length // 2):
            last_node = stack.pop()
            next_node = current.next

            current.next = last_node
            last_node.next = next_node
            current = next_node
        current.next = None
