class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Brute Force: For each num in nums, loop through the rest of the list to see if that number
        appears again. If you make it through the whole list for each number, then there are no
        duplicates.
            Time: O(n^2)
            Space: O(1)

        Optimized: Use a hashset with O(1) lookup/existence. Keep track of the ones seen so far.
        If you encounter one that has been seen already, there is a duplicate so return True.
        If you make it through the entire list without seeing a duplicate in seen, there is 
        no duplicate so return False.
            Time: O(n)
            Space: O(n)
        """

        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False