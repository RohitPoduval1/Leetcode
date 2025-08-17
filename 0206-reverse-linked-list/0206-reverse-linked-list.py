# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        OG:        1 -> 2 -> 3 -> None
        Reversed:  None <- 1 <- 2 <- 3
        """
        prev = None
        curr = head

        while curr:
            temp = curr.next  # keep the connection to the rest of the list

            curr.next = prev  # the actual reversal

            # Updating variables to keep progressing
            prev = curr
            curr = temp
        
        # When the loop exits, curr is None leading to prev being the new head of the reversed list
        return prev
        