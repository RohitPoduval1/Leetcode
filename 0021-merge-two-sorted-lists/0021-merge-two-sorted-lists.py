# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. Choose the smaller of the 2 heads to start with
        2. Compare the one we are on's next node to the other list's node
            Same? Does not matter which we choose
            Otherwise take the smaller one and connect it
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        list1_curr = list1
        list2_curr = list2
        curr = None
        dummy = ListNode()

        while list1_curr is not None and list2_curr is not None:
            if list1_curr.val <= list2_curr.val:
                list1_rest = list1_curr.next
                if curr is None:
                    curr = list1_curr
                    dummy.next = curr
                else:
                    curr.next = list1_curr
                    curr = curr.next
                list1_curr = list1_rest
            else:
                list2_rest = list2_curr.next
                if curr is None:
                    curr = list2_curr
                    dummy.next = curr
                else:
                    curr.next = list2_curr
                    curr = curr.next
                list2_curr = list2_rest

        ### Reached the end of one list so take the other in its entirety ###
        curr.next = list1_curr if list1_curr else list2_curr

        # Now we have built the sorted list in curr but we are at the tail
        return dummy.next