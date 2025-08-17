# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        OG:        1 -> 2 -> 3 -> None
                   1 <- 2 <- 3 <- None
                   3 -> 2 -> 1

        val=1
        next=2

        val=2
        next=3

        val=3
        next=None

        prev_node = None
        """
        if head is None:
            return None
        
        prev_node = None
        curr_node = head
        while curr_node is not None:
            # store pointer to next node since we will be changing pointers
            new_curr = curr_node.next

            # reverse the list by pointing to the previous node
            curr_node.next = prev_node

            # update the prev_node
            prev_node = curr_node

            # update curr_node to progress
            curr_node = new_curr
        
        return prev_node

        
