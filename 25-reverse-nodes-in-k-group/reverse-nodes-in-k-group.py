# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head, k):
            prev, curr = None, head
            while k > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k -= 1
            return prev  # new head after reversal

        # Count total nodes
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while count >= k:
            curr = prev_group.next
            next_group = curr

            # Move next_group pointer to start of next group
            for _ in range(k):
                next_group = next_group.next

            # Reverse k nodes
            new_head = reverseLinkedList(curr, k)
            prev_group.next = new_head
            curr.next = next_group  # Connect end of reversed group

            # Move prev_group pointer to end of this group
            prev_group = curr
            count -= k

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
