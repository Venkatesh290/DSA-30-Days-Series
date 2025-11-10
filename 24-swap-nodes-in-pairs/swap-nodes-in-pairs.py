# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next

            # Swapping nodes
            first.next = second.next
            second.next = first
            curr.next = second

            # Move to the next pair
            curr = first

        return dummy.next


    # Helper functions
    def list_to_linked(lst):
        dummy = ListNode()
        curr = dummy
        for num in lst:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

    def linked_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result