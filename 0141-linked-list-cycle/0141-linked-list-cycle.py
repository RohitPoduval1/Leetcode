# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Tortoise and Hare Algorithm (fast and slow pointers)
        * `fast` moves 2 steps and `slow` moves 1 step
        
        Eventually fast and slow will meet if there is a cycle.
        Otherwise fast will reach the end first.
        This is because slow increases the gap between fast and slow by 1
            (gap + 1)
        When fast moves (by 2) though, the gap decreases by 2
            (gap + 1 - 2)
        On a single iteration of the loop, the distance between fast and slow
            is reduced by 1.
        
        Time: O(n): Gap between fast and slow can only possibly be
            the length of the list - 1
        Space: O(1): Only 2 pointers, fast and slow regardless of problem size
        """
        slow, fast = head, head  # both start at same spot

        # Since fast will by definition always be faster than slow, it will
        # always explore the list first so we only need to focus on that.
        # Can't do fast.next.next in condition in case fast.next is None
        while fast and fast.next:
            # fast and slow caught up to each other
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        
        return False

    def hasCycleSuboptimal(self, head: Optional[ListNode]) -> bool:
        """
        SUBOPTIMAL
        Using a hashset to track which values we have seen. If we encounter a
        value we have seen before, we have already been there so there is a cycle.

        Time: O(n)
        Space: O(n)
        """
        visited = set()
        curr = head
        while curr is not None:
            if curr.val in visited:
                return True
            visited.add(curr.val)
            curr = curr.next
        
        return False