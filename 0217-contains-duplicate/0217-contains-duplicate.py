class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Optimal: Hashset to track seen numbers
        Time: O(n)
        Space: O(n)
        """
        seen = set()  # allows for O(1) lookup/existence
        for num in nums:
            if num in seen:  # we have already seen the number meaning
                return True  # there is a duplicate
            
            seen.add(num)   # no duplicate, so add the number to the ones we have seen already
        return False         # made it through nums without seeing any duplicates

    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     """
    #     Brute Force: Nested Loop
    #     Time: O(n^2)
    #     Space: O(1) 
    #     """
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == nums[j]:  # same number at different indices means
    #                 return True         # there is a duplicate
    #     return False
